from src.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def solve(problem_input: Input) -> str:
    datastream = problem_input.raw()

    for i in range(0, len(datastream) - 13):
        packet = set(datastream[i : i + 14])
        if len(packet) == 14:
            break

    return str(i + 14)


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
