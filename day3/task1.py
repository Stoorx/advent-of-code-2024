import re
from operator import mul

if __name__ == '__main__':
    mul_regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    result = 0
    with open('input.txt', 'r') as f:
        for m in mul_regex.finditer(f.read()):
             result += mul(*map(int, m.groups()))
    print(result)