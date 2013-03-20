# TODO generate final testing report

run-tests:
	@nosetests
	ps aux | grep 'python'

run-tests-with-coverage:
	@nosetests --with-coverage 
	ps aux | grep 'python'

graph:
	dot -T png docs/pyservice.gv -o docs/pyservice.png && eog docs/pyservice.png

todo:
	@ grep '# TODO' pyservice.py

update-dev-deps:
	pip install --upgrade nose
	pip install --upgrade coverage
	 
	
