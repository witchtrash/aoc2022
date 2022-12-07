from __future__ import annotations

from dataclasses import dataclass
from queue import SimpleQueue
from typing import Literal

from src.lib.util import Input, get_problem_input

problem_input: Input = get_problem_input()
test_input: Input = get_problem_input(test=True)


@dataclass
class File:
    size: int
    name: str


@dataclass
class Directory:
    name: str
    parent: Directory | None
    subdirectories: dict[str, Directory]
    contents: dict[str, File]

    def size(self) -> int:
        total = 0

        for file_name in self.contents.keys():
            total += self.contents[file_name].size

        if len(self.subdirectories) == 0:
            return total

        for directory_name in self.subdirectories.keys():
            total += self.subdirectories[directory_name].size()

        return total

    def tree(self, level: int = 0) -> None:
        print(f"{'  ' * level}{self.name} (dir, du={self.size()})")
        for directory_name in self.subdirectories.keys():
            self.subdirectories[directory_name].tree(level + 1)

        for file_name in self.contents:
            print(
                f"  {'  ' * level}{self.contents[file_name].name} (file, du={self.contents[file_name].size})"
            )


def get_directory_sizes(root: Directory) -> dict[str, int]:
    directory_queue: SimpleQueue[Directory] = SimpleQueue()
    directory_queue.put(root)

    size_map: dict[str, int] = {}

    while not directory_queue.empty():
        directory = directory_queue.get()

        size_map[directory.name] = directory.size()

        for directory_name in directory.subdirectories:
            directory_queue.put(directory.subdirectories[directory_name])

    return size_map


def solve(problem_input: Input) -> str:
    root = Directory(name="/", parent=None, subdirectories={}, contents={})
    current_directory: Directory = root
    executing: Literal["cd", "ls", None] = None
    total_disk_space = 70000000
    update_size = 30000000

    for line in problem_input.lines():
        if line[0] == "$":
            match line.split():
                case ["$", "ls"]:
                    executing = "ls"
                    continue
                case ["$", "cd", directory_name]:
                    if directory_name == "/":
                        current_directory = root
                    elif directory_name == "..":
                        if current_directory.parent is not None:
                            current_directory = current_directory.parent
                    else:
                        executing = "cd"
                        current_directory = current_directory.subdirectories[
                            directory_name
                        ]
                        executing = None
                        continue

        if executing == "ls":
            match line.split():
                case ["dir", directory_name]:
                    # Subdirectory
                    if directory_name not in current_directory.subdirectories:
                        current_directory.subdirectories[directory_name] = Directory(
                            name=directory_name,
                            parent=current_directory,
                            subdirectories={},
                            contents={},
                        )
                case [file_size, file_name]:
                    # File, no need to check
                    current_directory.contents[file_name] = File(
                        name=file_name, size=int(file_size)
                    )

    used_disk_space = root.size()
    remaining_disk_space = total_disk_space - used_disk_space
    required_disk_space = update_size - remaining_disk_space

    size_map = get_directory_sizes(root)
    sizes = sorted(list(size_map.values()))

    for size in sizes:
        if size >= required_disk_space:
            return str(size)

    return "No result."


def test() -> str:
    return str(solve(test_input))


def run() -> str:
    return str(solve(problem_input))
