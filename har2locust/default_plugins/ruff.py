import subprocess

from har2locust.plugin import outputstringprocessor


@outputstringprocessor
def ruff(py: str):
    p = subprocess.Popen(["ruff", "format", "-"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    assert p.stdin  # keep linter happy
    p.stdin.write(py)
    stdout, _stderr = p.communicate()
    assert (
        not p.returncode
    ), f"Ruff failed to format the output - perhaps your template is broken? unformatted output was: {py}"
    p = subprocess.Popen(
        [
            "ruff",
            "check",
            "--fix",
            "-q",
            "--exit-zero",  # ignore linting fails, we're most interested in applying fixes, and it is up to the user to examin errors
            "-",
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
    )
    assert p.stdin  # keep linter happy
    p.stdin.write(stdout)
    stdout, stderr = p.communicate()
    assert (
        not p.returncode
    ), f"Ruff failed to check/fix the output - perhaps your template is broken? unformatted output was: {stdout}"

    # for some reason the subprocess returns an extra newline, get rid of that
    return stdout[:-1]
