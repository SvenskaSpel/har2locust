clean:
	rm -rf build/

test:
	tox

build:
	rm -f dist/* && python3 setup.py sdist

up update_tests: 
	@echo rebuilding har2locust test files
	har2locust tests/inputs/login.har --plugins har2locust.extra_plugins.plugin_example > tests/outputs/login_plugin.py
	har2locust tests/inputs/login.har --disable-plugins rest.py > tests/outputs/login_disable_rest.py
	bash -c 'ls tests/inputs/ | xargs -I % basename % .har | xargs -I % bash -c "har2locust tests/inputs/%.har > tests/outputs/%.py"'

release: build
	twine upload dist/*
