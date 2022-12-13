# pylint: disable=redefined-outer-name
import json
import pathlib
import subprocess
import os
import pytest
import re
from har2locust.__main__ import __main__, process, render
from har2locust.argument_parser import get_parser

inputs_dir = pathlib.Path(__file__).parents[0] / "inputs"
outputs_dir = pathlib.Path(__file__).parents[0] / "outputs"

har_files = list(inputs_dir.glob("*.har"))
py_files = [outputs_dir / f.with_suffix(".py").name for f in har_files]


def h2l(*arguments, cwd=os.path.dirname(__file__)):
    return subprocess.Popen(
        arguments,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        cwd=cwd,
    )


with open(inputs_dir / "login.har") as f:
    har = json.load(f)


def test_har_file_not_found():
    with pytest.raises(FileNotFoundError):
        __main__(str(inputs_dir / "foo.har"))


def test_invalid_resource_types():
    proc = h2l(
        "har2locust",
        "--resource-types",
        "xhr,foo",
        "inputs/login.har",
    )
    _stdout, stderr = proc.communicate()
    assert proc.returncode == 1, f"Unexpected return code {proc.returncode}, stderr: {stderr}"
    assert "are not supported" in stderr


def test_render_syntax_error():
    with pytest.raises(
        SyntaxError,
        match=re.escape("invalid syntax (<unknown>, line 1)"),
    ):
        __main__([str(inputs_dir / "login.har"), "--template", "tests/broken_template.jinja2"])


def test_render_missing_template():
    with pytest.raises(
        Exception,
        match="Template this_doesnt_exist.jinja2 does not exist, neither in current directory nor as built in",
    ):
        __main__([str(inputs_dir / "login.har"), "--template", "this_doesnt_exist.jinja2"])


# writing py file in tests/output for manual inspection
@pytest.mark.parametrize("har_file, py_file", zip(har_files, py_files))
def test_output(har_file, py_file):
    with open(py_file, encoding="utf-8") as f:
        expected_output = f.read()
    proc = h2l(
        "har2locust",
        har_file,
        cwd=os.path.join(os.path.dirname(__file__), "../"),
    )
    stdout, stderr = proc.communicate()
    assert proc.returncode == 0, f"Bad return code {proc.returncode}, stderr: {stderr}"
    assert stdout == expected_output


def test_helptext():
    proc = h2l(
        "har2locust",
        "--help",
    )
    stdout, stderr = proc.communicate()
    assert proc.returncode == 0, f"Bad return code {proc.returncode}, stderr: {stderr}"
    assert "usage: har2locust" in stdout


def test_plugins():
    with open("tests/outputs/login_plugin.py", encoding="utf-8") as f:
        expected_output = f.read()
    proc = h2l(
        "har2locust",
        "tests/inputs/login.har",
        "--plugins",
        "tests/plugin_example.py",
        cwd=os.path.join(os.path.dirname(__file__), "../"),
    )
    stdout, stderr = proc.communicate()
    assert proc.returncode == 0, f"Bad return code {proc.returncode}, stderr: {stderr}"
    assert stdout == expected_output
    assert "self.reader.user" in stdout
    assert "self.customer" in stdout
    # test url timestamp rewriting function
    assert "self.rest_" in stdout
    assert "&_" not in stdout


def test_plugins_run_as_module():  # same as above test, but run as module
    with open("tests/outputs/login_plugin.py", encoding="utf-8") as f:
        expected_output = f.read()
    proc = h2l(
        "python3",
        "-m",
        "har2locust",
        "tests/inputs/login.har",
        "--plugins",
        "tests/plugin_example.py",
        cwd=os.path.join(os.path.dirname(__file__), "../"),  # needed to find .headerignore & .urlignore files
    )
    stdout, stderr = proc.communicate()
    assert proc.returncode == 0, f"Bad return code {proc.returncode}, stderr: {stderr}"
    assert stdout == expected_output
    assert "self.reader.user" in stdout
    assert "self.customer" in stdout
    # test url timestamp rewriting function
    assert "self.rest_" in stdout
    assert "&_" not in stdout


# this test is intended to be run AFTER regenerating the output using make update_tests
def test_locust_run():
    proc = h2l(
        "locust",
        "-f",
        "outputs/reqres.in.py",
        "-t",
        "4",
        "--headless",
    )
    _, stderr = proc.communicate()
    assert proc.returncode == 0, f"Bad return code {proc.returncode}, stderr: {stderr}"
    assert "--run-time limit reached" in stderr, stderr
