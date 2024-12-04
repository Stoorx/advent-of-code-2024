from collections import Counter

if __name__ == '__main__':
    left_list = []
    right_list = []
    with open('input.txt', 'r') as f:
        for line in f:
            left, right = map(int, line.split('   '))
            left_list.append(left)
            right_list.append(right)
    counter = Counter(right_list)
    print(sum(map(lambda n: n * counter[n], left_list)))