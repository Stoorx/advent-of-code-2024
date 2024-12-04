if __name__ == '__main__':
    left_list = []
    right_list = []
    with open('input.txt', 'r') as f:
        for line in f:
            left, right = map(int, line.split('   '))
            left_list.append(left)
            right_list.append(right)
    left_list.sort()
    right_list.sort()
    print(sum(map(lambda l,r: abs(r - l), left_list, right_list)))
