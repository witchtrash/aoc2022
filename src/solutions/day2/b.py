from __future__ import annotations

from enum import Enum
from typing import Literal, Tuple, cast

from src.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


TShape = Literal["rock", "paper", "scissors"]
TInputOpponent = Literal["A", "B", "C"]
TInputResponse = Literal["X", "Y", "Z"]


class Shape:
    type: TShape
    beats: TShape
    weakness: TShape
    value: int

    def __init__(self, type: TShape) -> None:
        self.type = type

        match type:
            case "rock":
                self.value = 1
                self.beats = "scissors"
                self.weakness = "paper"
            case "paper":
                self.value = 2
                self.beats = "rock"
                self.weakness = "scissors"
            case "scissors":
                self.value = 3
                self.beats = "paper"
                self.weakness = "rock"

    def compare(self, opponent: Shape) -> int:
        if self.beats == opponent.type:
            return self.value + 6
        elif opponent.beats == self.type:
            return self.value
        return self.value + 3

    def __repr__(self) -> str:
        return f"{self.type} ({self.value})"


def get_opponent_shape(input: TInputOpponent) -> Shape:
    match input:
        case "A":
            return Shape("rock")
        case "B":
            return Shape("paper")
        case "C":
            return Shape("scissors")


def get_outcome_shape(input: TInputResponse, opponent: Shape) -> Shape:
    match input:
        case "X":
            return Shape(opponent.beats)
        case "Y":
            return Shape(opponent.type)
        case "Z":
            return Shape(opponent.weakness)


def solve(problem_input: Input) -> str:
    score = 0

    for line in problem_input.lines():
        split = line.split()

        opponent = get_opponent_shape(cast(TInputOpponent, split[0]))
        response = get_outcome_shape(cast(TInputResponse, split[1]), opponent)

        score += response.compare(opponent)

    return str(score)


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
