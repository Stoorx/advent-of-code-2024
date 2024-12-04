from itertools import pairwise


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        safe_counter = 0
        for line in f:
            differences: list[int] = [a - b for a, b in pairwise(map(int, line.split(' ')))]
            if all(1 <= abs(d) <= 3 for d in differences) and all(a * b >= 0 for a,b in pairwise(differences)):
                safe_counter += 1
        print(safe_counter)

