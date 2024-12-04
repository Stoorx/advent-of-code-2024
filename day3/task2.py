import re
from operator import mul

if __name__ == '__main__':
    mul_regex = re.compile(r"(?P<op>do(?:n't)?|mul)\((?:(\d{1,3}),(\d{1,3}))?\)")
    result = 0
    enabled = True
    with open('input.txt', 'r') as f:
        for m in mul_regex.finditer(f.read()):
            match m.group('op'):
                case 'mul':
                    if enabled:
                        result += int(m.group(2)) * int(m.group(3))
                case 'do':
                    assert m.group(2) is None and m.group(3) is None
                    enabled = True
                case "don't":
                    assert m.group(2) is None and m.group(3) is None
                    enabled = False

    print(result)
