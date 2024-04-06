PY_MODULES = arraylist hash_map

test-mypy:  # typing check
	mypy $(PY_MODULES)

test-pylint:
	pylint -f parseable \
		--rcfile=${RCFILE} \
		-j 4 \
		$(PY_MODULES)

test-unit:
	python -m unittest discover test/

coverage:
	coverage run --source=. -m unittest discover test/
	coverage report --fail-under=80
	coverage html
