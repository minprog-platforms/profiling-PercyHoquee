## Installation

This project requires Python version 3.7 or later. To install all dependencies run: 

```
pip3 install -r requirements.txt
```

> if the any of the commands below fail, do make sure all required dependencies are installed via `pip3 install -r requirements.txt`. Alternatively, if for instance the `mypy` command is not found, try `python3 -m mypy` instead.

## How to run

```
$ python3 solve.py -h
usage: solve.py [-h] [-n NUMBER_OF_RUNS] puzzle

Solve a sudoku puzzle.

positional arguments:
  puzzle             identifier of the puzzle to be solved

optional arguments:
  -h, --help         show this help message and exit
  -n NUMBER_OF_RUNS  number of runs
```

For instance, to solve the fourth puzzle ten times, run:

```
python3 solve.py -n 10 4
```

## Testing

To test the implementation simply run `pytest` in the root folder of the project.

```
pytest
```


## Type-checking

To check the types of the implementation run the following in the root folder of the project:

```
mypy *.py
```

## Formatting

To check the formatting of the code use:

```
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

## Profiling

To create a profile run:

```
python3 -m cProfile -o solve.prof solve.py -n 10 4
```

This creates a file called `solve.prof` that can then be inspected through:

```
snakeviz solve.prof
```
