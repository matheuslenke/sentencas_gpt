.PHONY: run

run: install_dependencies
	python -m main infer

install_dependencies:
	pip install -r requirements.txt