# pylint: disable=redefined-outer-name
import json
import pathlib
import subprocess
import os
import pytest
from har2locust.main import main, process, rendering
from libcst import ParserSyntaxError

inputs_dir = pathlib.Path(__file__).parents[0] / "inputs"
outputs_dir = pathlib.Path(__file__).parents[0] / "outputs"

har_files = list(inputs_dir.glob("*.har"))
py_files = [outputs_dir / f.with_suffix(".py").name for f in har_files]

har_file = har_files[0]
py_file = py_files[0]

with open(har_file) as f:
    har = json.load(f)


def test_har_file_not_found():
    har_file_foo = inputs_dir / "foo.har"
    with pytest.raises(FileNotFoundError):
        main(str(har_file_foo))


def test_preprocessing_unsupported_resource_type():
    with pytest.raises(NotImplementedError, match="are not supported"):
        process(har, resource_type=["xhr", "foo", "bar"])


def test_rendering_syntax_error():
    with pytest.raises(SystemExit):
        rendering("tests/broken_template.jinja2", process(har))


def test_rendering_missing_template():
    with pytest.raises(
        Exception,
        match="Template this_doesnt_exist.jinja2 does not exist, neither in current directory nor as built in",
    ):
        rendering("this_doesnt_exist.jinja2", process(har))


# writing py file in tests/output for manual inspection
@pytest.mark.parametrize("har_file, py_file", zip(har_files, py_files))
def test_output(har_file, py_file):
    with open(py_file, encoding="utf-8") as f:
        expected_output = f.read()
    proc = subprocess.Popen(
        ["har2locust", har_file],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        cwd=os.path.join(os.path.dirname(__file__), "../"),
    )
    stdout, stderr = proc.communicate()
    assert proc.returncode == 0, f"Bad return code {proc.returncode}, stderr: {stderr}"
    assert stdout.strip() == expected_output.strip()


def test_helptext():
    proc = subprocess.Popen(
        ["har2locust", "--help"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    )
    stdout, stderr = proc.communicate()
    assert proc.returncode == 0, f"Bad return code {proc.returncode}, stderr: {stderr}"
    assert "usage: har2locust" in stdout


def test_plugins():
    har_file = "tests/inputs/reqres.in.har"
    py_file = "tests/outputs/reqres_plugin.in.py"
    with open(py_file, encoding="utf-8") as f:
        expected_output = f.read()
    proc = subprocess.Popen(
        ["har2locust", har_file, "--plugins", "tests/plugin_example.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        cwd=os.path.join(os.path.dirname(__file__), "../"),
    )
    stdout, stderr = proc.communicate()
    assert proc.returncode == 0, f"Bad return code {proc.returncode}, stderr: {stderr}"
    assert stdout.strip() == expected_output.strip()
    assert "NewName" in stdout
    assert "renamed_function(self)" in stdout
    assert "hello" in stderr, stderr


# this test is intended to be run AFTER regenerating the output using make update_tests
def test_locust_run():
    proc = subprocess.Popen(
        ["locust", "-f", "outputs/reqres.in.py", "-i", "1", "--headless"],
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        cwd=os.path.join(os.path.dirname(__file__)),
    )
    _, stderr = proc.communicate()
    assert proc.returncode == 0, f"Bad return code {proc.returncode}, stderr: {stderr}"
    assert "Iteration limit reached" in stderr, stderr
