from har2locust.plugin import outputstringprocessor
import subprocess


@outputstringprocessor
def process_output(py):
    p = subprocess.Popen(["black", "-q", "-"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    assert p.stdin  # keep linter happy
    p.stdin.write(py)
    stdout, _stderr = p.communicate()
    assert (
        not p.returncode
    ), f"Black failed to format the output - perhaps your template is broken? unformatted output was: {py}"

    # for some reason the subprocess returns an extra newline, get rid of that
    return stdout[:-1]
