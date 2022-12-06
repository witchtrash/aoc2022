import re

from src.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def parse_crate_input(input: list[str]) -> list[list[str]]:
    crates: list[list[str]] = []
    line_length = len(input[0])

    for line in input:
        if line[1] == "1":
            number_of_crates = int(line[-2])
            crates = [[] for x in range(number_of_crates)]
            break

    for line in input:
        i = 0

        if line[1] == "1":
            break
        for c in range(1, line_length, 4):
            crate = line[c]

            if crate != " ":
                crates[i].insert(0, crate)
            i += 1

    return crates


def solve(problem_input: Input) -> str:
    crates = parse_crate_input(problem_input.raw(strip=False).split("\n"))

    for line in problem_input.lines():
        match = re.search(r"move (\d+) from (\d+) to (\d+)", line)
        if match:
            steps = int(match.group(1))
            from_number = int(match.group(2)) - 1
            to_number = int(match.group(3)) - 1

            for _ in range(steps):
                crate = crates[from_number].pop()
                crates[to_number].append(crate)

    crate_str = ""

    for crate_list in crates:
        crate_str += crate_list.pop()

    return crate_str


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
