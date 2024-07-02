if __name__ == '__main__':
    N = int(input())
    li = []
    for i in range(0, N):
        cmd = list(input().split())
        if (cmd[0] == "insert "):
            li.insert(int(cmd[1]), int(cmd[2]))
        if (cmd[0] == "print "):
            print(li)
        if (cmd[0] == "remove"):
            li.remove(int(cmd[1]))
        if (cmd[0] == "append "):
            li.append(int(cmd[1]))
        if (cmd[0] == "sort "):
            li.sort()
        if (cmd[0] == "pop "):
            li.pop()
        if (cmd[0] == "reverse "):
            li.reverse()
