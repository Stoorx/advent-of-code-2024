from itertools import pairwise
from typing import Iterable


def check(report: Iterable[int]) -> bool:
    diffs: list[int] = [a - b for a, b in pairwise(report)]
    return all(1 <= abs(d) <= 3 for d in diffs) and all(a * b >= 0 for a, b in pairwise(diffs))

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        safe_counter = 0
        for line in f:
            levels = list(map(int, line.split(' ')))
            if check(levels):
                safe_counter += 1
            else:
                for i in range(len(levels)):
                    if check(levels[:i] + levels[i + 1:]):
                        safe_counter += 1
                        break
        print(safe_counter)