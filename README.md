# Sudoku Solver

This is a sudoku solver. 

# Cloning

You can clone this repository to your machine using either SSH or HTTPS.

* By HTTPS: (be aware you'll have to generate git credentials)

    `git clone https://github.com/tim-den-dulk/sudoku.git`

* by SSH: (make sure to generate an ssh key and add it to Github)

    `git clone <your-username>@github.com:tim-den-dulk/sudoku.git`
    
# Set-up

to setup the project you'll need to activate your virtual environment.
This project makes use of poetry for dependency management.

1. Create your python virtual environment:

    `python -m venv env`
    
2. Activate this virtual environment:

    `env\Scripts\activate` 
    
3. Install poetry and the project dependencies:

    `pip install poetry`
    
    `poetry install`
    
poetry will now install the correct dependencies as specified in the pyproject.toml and poetry.lock files.

## Testing

We use pytest to run our tests. Pycharm can configure this for you automatically.
Should you want to run this manually instead, you'll have to add the home directory to your pythonpath and run pytest.

For Windows:

    set PYTHONPATH=C:\<path>\<to>\<repository>
    cd <path>\<to>\<repository>\tests
    pytest
    
For Linux:
    
    export PYTHONPATH=/<path>/<to>/<repository>
    cd <path>/<to>/<repository>/tests
    pytest

## Pre-Commit

This project makes use of pre-commit.
To setup pre-commit run the following command:

    pre-commit install
    
pre-commit will automatically run Black, Flake8 and Isort before each commit you make.