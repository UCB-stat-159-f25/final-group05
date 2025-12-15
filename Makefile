.PHONY : env all help

## env       :create a new environment from environment.yml, or update it if it already exists
env : environment.yml
	conda env update --name finalproj --file environment.yml --prune

## all       : runs all notebooks
all : pdf_builds/main.pdf pdf_builds/word-analysis.pdf pdf_builds/LLM.pdf

pdf_builds/main.pdf : main.ipynb
	jupyter nbconvert --to pdf --execute main.ipynb --output-dir pdf_builds

pdf_builds/word-analysis.pdf : word-analysis.ipynb
	jupyter nbconvert --to pdf --execute word-analysis.ipynb --output-dir pdf_builds

pdf_builds/LLM.pdf : LLM.ipynb
	jupyter nbconvert --to pdf --execute LLM.ipynb --output-dir pdf_builds

help : Makefile
	@sed -n 's/^##//p' $<