# TODO generate final testing report

test-unittest:
	@ echo '***************************'
	@ echo '*       Unittests         *'
	@ echo '***************************'
	python tests/test_runner.py
	python tests/test_utils.py
	python tests/test_core.py
	python tests/test_process1.py
	python tests/test_process2.py

test-doctest:
	@ echo '***************************'
	@ echo '*       Doctests          *'
	@ echo '***************************'
	python -m doctest tests/test_runner.md

test-all:
	make test-unittest
	make test-doctest

graph:
	dot -T png docs/pyservice.gv -o docs/pyservice.png && eog docs/pyservice.png

todo:
	@ grep '# TODO' pyservice.py
	
