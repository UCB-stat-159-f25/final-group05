[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/sSkqmNLf)

[MyST Website](https://ucb-stat-159-f25.github.io/final-group05/)

To check out the Binder build, go to [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/final-group05/HEAD)

# Final Project: Analysis of Executive Orders
In this project, we analyze executive orders (EOs) from 1994–2025. The dataset is available on the U.S. Government Open Data Portal and is also included in this repository as executive_orders.csv. We perform several frequency-based analyses, including examining the number of EOs issued over time and changes in the prevalence of different EO types. We also identify a data integrity issue related to publication delays when comparing signing and publication dates. In addition, we explore a lightweight natural language processing application by fine-tuning a small pretrained language model on executive order titles. This experiment illustrates how historical EO titles can be used to generate plausible future EO titles and allows us to compare model outputs before and after fine-tuning. Most analyses are presented in dedicated analysis notebooks, with results summarized and discussed in main.ipynb.

# Repository Structure
The repository is structured as follows:
- `EO_processing/`: Python Functions for data processing
- `tests/`: Tests for fucntions in `EO_processing/`
- `outputs/`: Outputs from word-analysis.ipynb and LLM.ipynb
- `executive_orders.csv`: The Executive Order data to be analyzed
- `main.ipynb`: Main project notebook providing figures and analysis
- `word-analysis.ipynb`: Notebook containing further data analysis
- `LLM.ipynb`: Notebook containing LLM training 
- `environment.yml`: Environment file with required packages
- `Makefile`: Makefile to create or update the environment and run all notebooks

# Setup and Installation
1. Clone the repository:
```bash
git clone https://github.com/UCB-stat-159-f25/final-group05.git
cd final-group05
```
2. Create and activate the environment:
```bash
make env
conda activate finalproj
```
3. Install the IPython Kernel with the environment:
```bash
python -m ipykernel install --user --name finalproj --display-name "IPython - finalproj"
```
# Usage
To execute all notebooks, run:
```bash
make all
```

# Package_structure
The `EO_processing` package contains functions to process and verify the executive order data. The package contains the following functions:
- From `additions.py`:
	1. `add_years(df, col)`: Parses column in given dataframe to add 'year' column
	2. `add_months(df, col)`: Parses column in given dataframe to add 'month' column
	3. `add_publication_delay(df, signing_col="signing_date", publication_col="publication_date",output_col="days_diff")`: Adds a column with the difference in days between signing and publication dates
	4. `add_revoked_flag(df, disposition_col="disposition_notes", output_col="is_revoked")`: Parses column in given dataframe to add 'is_revoked' column
	5. `add_amends_flag(df, disposition_col="disposition_notes", output_col="is_amendment")`: Parses column in given dataframe to add 'is_amendment' column 
- From `verify.py`:
	1. `verify_type(df, desired)`: Counts number of rows in dataframe where type column doesn't match desired input
	2. `fix_type(df, desired)`: Returns dataframe with only rows where type column matches desired input
	3. `verify_subtype(df, desired)`: Counts number of rows in dataframe where subtype column doesn't match desired input
	4. `fix_subtype(df, desired)`: Returns dataframe with only rows where subtype column matches desired input

# Testing
To test the functions in the package, navigate to the root directory of the project and run:
```bash
PYTHONPATH=./ pytest
```

## License
This project follows a reproducible research licensing standard, as recommended by Victoria Stodden in *Enabling Reproducible Research: Licensing Scientific Innovation*.

- Code in this repository is licensed under the BSD 3-Clause License.
- Data included in this repository is shared under the Creative Commons Attribution 4.0 International (CC BY 4.0) license, subject to the original terms of the U.S. Government Open Data Portal.
- Text, figures, and media are licensed under CC BY 4.0, which permits reuse with appropriate attribution.


