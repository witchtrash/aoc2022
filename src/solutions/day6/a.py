from src.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


def solve(problem_input: Input) -> str:
    datastream = problem_input.raw()

    for i in range(0, len(datastream) - 3):
        packet = set(datastream[i : i + 4])
        if len(packet) == 4:
            break

    return str(i + 4)


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
