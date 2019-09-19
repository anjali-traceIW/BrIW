# BrIW v0.1

An app to take your drink rounds.

## Setting up and running

Requires python3. Install with homebrew `brew install python` or your favourite package manager.

Tests use the unittest testing library and pytest to run the tests. Install with pip using `pip3 install unittest` and `pip3 install pytest`.

Data files for people, drinks, and rounds are csv files in data/. 

To run: 

- from command line: in the root directory, run `python3 -m src.brIW1`
- otherwise: the main script is src/brIW.py so run this in your IDE of choice 

Running tests:

`python3 -m pytest`

To get test coverage:

`pytest -m src --cov=src test`

## How to contribute

Fork this repository. Do some things. Submit a pull request to master. Thanks!

