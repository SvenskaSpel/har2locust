# pylint: disable=redefined-outer-name
import json
import pathlib
import subprocess
import os
import pytest
import re
from har2locust.__main__ import __main__, main, process, rendering

inputs_dir = pathlib.Path(__file__).parents[0] / "inputs"
outputs_dir = pathlib.Path(__file__).parents[0] / "outputs"

har_files = list(inputs_dir.glob("*.har"))
py_files = [outputs_dir / f.with_suffix(".py").name for f in har_files]


def h2l(*arguments):
    return subprocess.Popen(
        arguments,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        cwd=os.path.dirname(__file__),
    )


with open(inputs_dir / "login.har") as f:
    har = json.load(f)


def test_har_file_not_found():
    har_file_foo = inputs_dir / "foo.har"
    with pytest.raises(FileNotFoundError):
        main(str(har_file_foo))


def test_helptext():
    proc = h2l("har2locust", "--resource-types xhr,foo", "tests/inputs/login.har")
    _stdout, stderr = proc.communicate()
    assert proc.returncode == 1, f"Unexpected return code {proc.returncode}, stderr: {stderr}"
    assert "are not supported" in stderr


def test_rendering_syntax_error():
    with pytest.raises(
        SyntaxError,
        match=re.escape("invalid syntax (<unknown>, line 1)"),
    ):
        main(str(inputs_dir / "login.har"), template_name="tests/broken_template.jinja2")


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
    proc = h2l("har2locust", "--help")
    stdout, stderr = proc.communicate()
    assert proc.returncode == 0, f"Bad return code {proc.returncode}, stderr: {stderr}"
    assert "usage: har2locust" in stdout


def test_plugins():
    har_file = "tests/inputs/login.har"
    py_file = "tests/outputs/login_plugin.py"
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
    assert "self.reader.user" in stdout
    assert "self.customer" in stdout
    # test url timestamp rewriting function
    assert "self.rest_" in stdout
    assert "&_" not in stdout


# this test is intended to be run AFTER regenerating the output using make update_tests
def test_locust_run():
    proc = h2l("locust", "-f", "outputs/reqres.in.py", "-i", "1", "--headless")
    _, stderr = proc.communicate()
    assert proc.returncode == 0, f"Bad return code {proc.returncode}, stderr: {stderr}"
    assert "Iteration limit reached" in stderr, stderr
