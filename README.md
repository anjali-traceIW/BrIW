# BrIW v0.1

An app to take your drink rounds.

## Setting up and requirements

Requires python3. Install with homebrew `brew install python` or your favourite package manager.

Tests use the unittest testing library and pytest to run the tests. Install with pip using `pip3 install unittest` and `pip3 install pytest`.

See `requirements.txt` for any further pip packages to install. Can use `pip install -r requirements.txt` to install everything contained at once.

Expects database connection parameters to be in a file called `param.py` in `/src/cls/` with contents as follows:

```python
hostname = "hostname"
username = "username"
password = "password"
database_name = "db_name"
```

## How to Run

### Command line application

- from command line: in the root directory, run `python3 -m src.brIW1`
- otherwise: the main script is `/src/brIW.py` so run this in your IDE of choice 

### API

From command line at root directory:

```bash
python3 -m src.api.api
```

Is currently hosted on port 8081.

### Tests

Tests are in `/test`. To run all tests:

```bash
python3 -m pytest
```

To get test coverage:

```bash
pytest -m src --cov=src test
```

## How to contribute

Fork this repository. Do some things. Submit a pull request to master. Thanks!

