from string import ascii_letters

from src.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def solve(problem_input: Input) -> str:
    priority = 0
    priority_map = {k: i + 1 for i, k in enumerate(ascii_letters)}

    rucksacks: list[set[str]] = [set(x) for x in problem_input.lines()]

    for i in range(0, len(rucksacks) - 2, 3):
        intersection = (
            rucksacks[i].intersection(rucksacks[i + 1]).intersection(rucksacks[i + 2])
        )

        for item in intersection:
            priority += priority_map[item]

    return str(priority)


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
