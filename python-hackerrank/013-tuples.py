#python 2 
if __name__ == '__main__':
    n = int(raw_input()) # type: ignore
    integer_list = map(int, raw_input().split()) # type: ignore
    print(hash(tuple(integer_list)))