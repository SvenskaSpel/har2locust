import json
import pathlib

import pytest
from har2locust import __version__
from har2locust.main import main, preprocessing, rendering

inputs_dir = pathlib.Path(__file__).parents[0] / 'inputs'
outputs_dir = pathlib.Path(__file__).parents[0] / 'outputs'

har_files = list(inputs_dir.glob('*.har'))
py_files = [outputs_dir / f.with_suffix('.py').name for f in har_files]

har_file = har_files[0]
py_file = py_files[0]

with open(har_file) as f:
    har = json.load(f)


def test_version():
    assert __version__ == '0.1.1'


def test_har_file_not_found():
    har_file_foo = inputs_dir / 'foo.har'
    with pytest.raises(FileNotFoundError):
        main(har_file_foo, py_file)


def test_har_file_wrong_suffix():
    foo_file = har_file.with_suffix('.foo')
    with open(foo_file, 'w'):
        pass
    with pytest.raises(IOError, match='use an ".har" file'):
        main(foo_file, py_file)
    foo_file.unlink()



def test_py_file_already_exists_overwrite_false():
    with open(py_file, 'w'):
        pass
    with pytest.raises(IOError):
        main(har_file, py_file, overwrite=False)
    assert py_file.is_file()
    py_file.unlink()


def test_py_file_already_exists_overwrite_true():
    with open(py_file, 'w'):
        pass
    main(har_file, py_file, overwrite=True)
    py_file.unlink()


def test_preprocessing_unsupported_resource_type():
    with pytest.raises(NotImplementedError, match='are not supported'):
        preprocessing(har, resource_type=['xhr', 'foo', 'bar'])


def test_rendering_without_preprocess():
    with pytest.raises(ValueError, match='har dict has wrong format.'):
        rendering(har)


def test_rendering_syntax_error():
    with pytest.raises(SyntaxError, match='cannot parse har'):
        rendering(
            preprocessing(har),
            template_dir=pathlib.Path(__file__).parents[0],
            template_name='broken_template.jinja2',
        )


# writing py file in tests/output for manual inspection
@pytest.mark.parametrize("har_file, py_file", zip(har_files, py_files))
def test_main(har_file, py_file):
    main(har_file, py_file, overwrite=True)
