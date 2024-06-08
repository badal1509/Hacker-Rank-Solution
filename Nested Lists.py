if __name__ == '__main__':
    record=[]
    lis2=[]
    nam=[]
    rd=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name,score])
        lis2.append(score)
    lis2.sort()
    for i in lis2:
        if i not in rd:
            rd.append(i)
    sl=rd[1]
    for n,s in record:
        if s==sl:
            nam.append(n)
    nam.sort()
    for i in nam:
        
        print(i)
