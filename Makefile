init: clean
	python3 -m pip install -r requirements-dev.txt

test-unit:
	python3 -m pytest ${filter} --capture=sys -v

debug-test-unit:
		python3 -m pytest --pdb ${filter} --capture=sys -v

test-unit-cov:
	python3 -m pytest ${filter} \
		--cov-config .coveragerc \
		--cov-branch \
		--cov-report term-missing \
		--cov=atlassian_cli \
		tests

install-develop: clean
	python3 setup.py develop

test: test-unit-cov

profile:
	kernprof -v -l $(command)

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
