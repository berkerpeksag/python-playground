.DEFAULT_GOAL := build

clean:
	rm -r build/
	rm -r *.egg-info
	rm *.so

build:
	python setup.py build
	python setup.py install

.PHONY: build clean
