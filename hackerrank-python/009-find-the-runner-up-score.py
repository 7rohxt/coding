if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lis = list(arr)
    max_score = -float('inf')
    for i in lis:
        if i > max_score:
            max_score = i
    second_max = -float('inf')
    for i in lis:
        if i < max_score and i > second_max:
            second_max = i
    print(second_max)