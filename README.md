# aoc2021

Advent of Code 2022

## Setup

Make sure you have poetry >=1.2.0 and Python 3.11 installed. I recommend using something like pyenv to manage your Python versions. pyenv can automatically pick up and install the version defined in `.python-version` with `pyenv install`. 

0. (Optionally): Install `Python 3.11.0a1` with `pyenv install`.
1. Spawn a new shell with `poetry shell`
2. Install dependencies with `poetry install`

## Running a solution

Run a solution with `./solve --day N --part a|b`

If you want to run against the test case, add the `--test` flag, e.g. `./solve --day 1 --part b --test`
