if __name__ == '__main__':
    N = int(input())
    list1 = []
    for _ in range(N):
        cmd = input().split()   
        if cmd[0] =='insert':
            i=int(cmd[1])
            e=int(cmd[2])
            list1.insert(i,e)
        elif cmd[0] == 'print':
            print(list1)
        elif cmd[0] == 'remove':
            e = int(cmd[1])
            list1.remove(e)
        elif cmd[0] == 'append':
            e = int(cmd[1])
            list1.append(e)
        elif cmd[0] == 'sort':
            list1.sort()
        elif cmd[0] == 'pop':
            list1.pop()
        elif cmd[0] == 'reverse':
            list1.reverse()