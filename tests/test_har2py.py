import json
import pathlib

import pytest
from har2py import __version__
from har2py.main import main

hars_dir = pathlib.Path(__file__).parents[0] / 'hars'

har_files = list(hars_dir.glob('*.har'))
har_file = har_files[0]
py_file = har_file.with_suffix('.py')


def test_version():
    assert __version__ == '0.1.0'


def test_har_file_not_found():
    har_file_foo = hars_dir / 'foo.har'
    with pytest.raises(FileNotFoundError):
        main(har_file_foo)


def test_har_file_wrong_suffix():
    foo_file = har_file.with_suffix('.foo')
    with pytest.raises(FileNotFoundError):
        main(foo_file)


def test_py_already_exists_overwrite_false():
    with open(py_file, 'w'):
        pass
    with pytest.raises(IOError):
        main(har_file, overwrite=False)
    py_file.unlink()


def test_py_already_exists_overwrite_true():
    with open(py_file, 'w'):
        pass
    main(har_file, overwrite=True)
    py_file.unlink()


@pytest.mark.parametrize('har_file', har_files)
def test_har2py(har_file):
    main(har_file, overwrite=True)
