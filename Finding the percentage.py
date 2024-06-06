if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks:
        if query_name==i:
            temp=0
            temp2=0
            for j in student_marks[i]:
                temp+=1
                temp2+=j
            print(format(temp2/temp,".2f"))
