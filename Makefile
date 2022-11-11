clean:
	rm -rf build/

test:
	tox

build:
	rm -f dist/* && python3 setup.py sdist

up update_tests: 
	@echo rebuilding har2locust test files
	har2locust tests/inputs/reqres.in.har --plugins tests/plugin_example.py > tests/outputs/reqres_plugin.in.py
	bash -c 'ls tests/inputs/ | xargs -I % basename % .har | xargs -I % bash -c "har2locust tests/inputs/%.har > tests/outputs/%.py"'

release: build
	twine upload dist/*
