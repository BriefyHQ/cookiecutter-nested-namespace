lint: ## check style with flake8
	flake8 tests setup.py

test: ## run tests quickly with the default Python
	py.test tests
