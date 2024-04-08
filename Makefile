all: clone index search

search: index
	python search.py

index: clone
	python index.py

clone:
	git clone https://github.com/datamade/how-to
