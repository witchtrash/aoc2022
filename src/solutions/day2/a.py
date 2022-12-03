from __future__ import annotations

from enum import Enum
from typing import Literal, cast

from src.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


TShape = Literal["rock", "paper", "scissors"]
TInput = Literal["A", "B", "C", "X", "Y", "Z"]


class Shape:
    type: TShape
    beats: TShape
    value: int

    def __init__(self, type: TShape) -> None:
        self.type = type

        match type:
            case "rock":
                self.value = 1
                self.beats = "scissors"
            case "paper":
                self.value = 2
                self.beats = "rock"
            case "scissors":
                self.value = 3
                self.beats = "paper"

    def compare(self, opponent: Shape) -> int:
        if self.beats == opponent.type:
            return self.value + 6
        elif opponent.beats == self.type:
            return self.value
        return self.value + 3


def get_shape(input: TInput) -> Shape:
    match input:
        case "A" | "X":
            return Shape("rock")
        case "B" | "Y":
            return Shape("paper")
        case "C" | "Z":
            return Shape("scissors")

    return None


def solve(problem_input: Input) -> str:
    score = 0

    for line in problem_input.lines():
        opponent, response = [get_shape(cast(TInput, x)) for x in line.split()]
        score += response.compare(opponent)

    return str(score)


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
