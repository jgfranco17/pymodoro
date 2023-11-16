<h1 align="center">PYMODORO</h1>

<h3 align="center">A CLI-Based Pomodoro Timer App</h3>

<div align="center">
<br />

![STATUS](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge) ![LICENSE](https://img.shields.io/badge/license-BSD3Clause-blue?style=for-the-badge)

</div>

---

## Table of Contents

- [About](#about)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Authors](#authors)

## About <a name="about"></a>

### Overview

Pymodoro is a simple command-line interface (CLI) tool for implementing the Pomodoro Technique—a time management method that uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks.

## Prerequisites <a name="prerequisites"></a>

The following must be installed on the host machine:

- [Python 3.9](https://github.com/pyenv/pyenv) or above

It is highly recommended to use `pyenv` to manage Python versions. This project is built in Ubuntu 22.04, but should also work on MacOS, as well as other Linux distros.

### Python dependencies

To get started with this project for development purposes, clone the repository to your local machine and install the required dependencies.

```bash
git clone https://github.com/jgfranco17/pymodoro.git
cd pymodoro
pip install -r requirements.txt
```

## Usage <a name="usage"></a>

To use Pymodoro in your terminal, simply run the command as follows:

```bash
python pomodoro.py --work 30 --break-time 10
```

This command will set the work duration to 30 minutes and the break duration to 10 minutes.

## Testing <a name = "testing"></a>

### Running unittest suite

In order to run diagnostics and unittests, first install the testing dependencies. This will allow you to utilize the full capacity of the test modules we have built.

```bash
pip install -r requirements-test.txt
```

To run the full test suite, run the Makefile command as follows:

```bash
cd Pymodoro
make test
```

### Using PyTest

You can run these tests using the [PyTest](https://docs.pytest.org/en/7.3.x/) CLI tool. To run all tests in the directory containing the test files, navigate to the directory and enter `pytest` in the command line; for added verbosity, add the `-vv` flag after. To run a specific test file, enter `pytest <filename>`.

```bash
# Run all tests in the testing module with verbose detail
cd pymodoro
pytest -vv

# Or, run a specific test file
cd pymodoro/tests
pytest -v <filename>.py
```

This will run the specified test module and generates a detailed result report in the terminal.

### Why these tests are important

Running these unittests is necessary to ensure that the code is functioning as expected and meeting the requirements of the design specification. The unittests are designed to test each function and method of the code and to identify any errors or unexpected behavior. By testing the code using these PyTest unittests, we can ensure that the code meets the specified requirements and that any changes made to the code do not introduce new bugs or errors.

In addition, these tests can be automated to run on every code change, allowing us to quickly identify any issues that may arise and enabling us to maintain a high level of code quality.

In essence, running these PyTest unittests is a critical part of the software QA process and helps to ensure that our code is robust, reliable, and meets the needs of our end-users before the product hits deployment.

## Authors <a name = "authors"></a>

- [Chino Franco](https://github.com/jgfranco17)
