.PHONY: all lint test install dev clean distclean python-tests r-tests

PYTHON ?= python

all: ;

lint:
	q2lint
	flake8

test: r-tests python-tests

python-tests:
	py.test

r-tests:
	Rscript -e "library(testthat); test_dir('q2_r_example_plugin/tests/R')"

install: all
	pip install .

dev: all
	pip install -e .

clean: distclean

distclean: ;
