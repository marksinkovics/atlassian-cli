# Development

This project has built on the top of the latest python 3 version

## Prerequisite

* install the latest Python3
	* macOS: `brew install python3`
	* Windows: download and install it from the [official site](https://www.python.org/downloads/)

## After clone

The project contains a Makefile which can help to simplify the development workflow. Unfortunately it only works on Unix systems.  

1. Run `make init` : It installs / updates the required pip pacakges

## During the development

* `make install-develop` Install it locally and use commands systemwide
* `make clean` Remove unecessary cache files
* `make test-unit` Run all unit tests
** use `filter=<path/to/test>` to run only filtered tests e.g. `make filter="tests/service/test_service.py::ServiceTestCase" test-unit`
* `make test-unit-cov`  Run all test and measure the coverage
* `make test` it does the same as `make test-unit-cov`




