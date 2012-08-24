test:
	python tests/test_runner.py
	python tests/test_utils.py
	python tests/test_core.py
	python tests/test_process1.py
	python tests/test_process2.py

graph:
	dot -T png docs/pyservice.gv -o docs/pyservice.png && eog docs/pyservice.png

todo:
	grep TODO pyservice/*
	
