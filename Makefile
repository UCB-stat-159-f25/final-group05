.PHONY : env all help

## env       :create a new environment from environment.yml, or update it if it already exists
env : environment.yml
	conda env update --name ligo --file environment.yml --prune

## all       : runs all notebooks
all : %.ipynb
	jupyter nbconvert --to pdf $*.ipynb


help : Makefile
	@sed -n 's/^##//p' $<