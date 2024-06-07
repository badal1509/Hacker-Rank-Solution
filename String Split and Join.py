def split_and_join(line):
    li=list(line.split(" "))
    str1=""
    for i in li:
        if (i==li[-1]):
            str1+=i
            break
        str1=str1 + i +"-"
    return str1

