# TODO generate final testing report

tests:
	@nosetests

tests-with-coverage:
	@nosetests --with-coverage 

graph:
	dot -T png docs/pyservice.gv -o docs/pyservice.png && eog docs/pyservice.png

todo:
	@ grep '# TODO' pyservice.py

update-dev-deps:
	pip install --upgrade nose
	pip install --upgrade coverage
	 
	
