test:
	python tests/test_runner.py
	python tests/test_utils.py
	python tests/test_core.py

graph:
	dot -T png docs/pyservice.gv -o docs/pyservice.png && eog docs/pyservice.png
	
