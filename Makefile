.PHONY: env all pdfs help

## env : create/update the conda environment
env: environment.yml
	conda env list | grep -q finalproj || conda env create -n finalproj -f environment.yml
	conda env update --name finalproj --file environment.yml --prune

## all : execute all notebooks (reproducibility) using nbconvert
all:
	jupyter nbconvert --to notebook --execute main.ipynb --inplace
	jupyter nbconvert --to notebook --execute word-analysis.ipynb --inplace
	jupyter nbconvert --to notebook --execute LLM.ipynb --inplace

## pdfs : render PDFs using MyST into pdf_builds/
pdfs:
	mkdir -p pdf_builds
	myst build main.ipynb --pdf
	myst build word-analysis.ipynb --pdf
	myst build LLM.ipynb --pdf
	# Copy the PDFs from _build to pdf_builds 
	cp _build/exports/main.pdf pdf_builds/main.pdf || true
	cp _build/exports/word-analysis.pdf pdf_builds/word-analysis.pdf || true
	cp _build/exports/llm.pdf pdf_builds/LLM.pdf || true

help:
	@sed -n 's/^##//p' Makefile
