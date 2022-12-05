from string import ascii_letters

from src.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def solve(problem_input: Input) -> str:
    priority = 0
    priority_map = {k: i + 1 for i, k in enumerate(ascii_letters)}

    rucksacks: list[tuple[set[str], set[str]]] = [
        (set(x[: len(x) // 2]), set(x[len(x) // 2 :])) for x in problem_input.lines()
    ]

    for sack in rucksacks:
        intersection = sack[0].intersection(sack[1])
        for item in intersection:
            priority += priority_map[item]

    return str(priority)


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
