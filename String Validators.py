if __name__ == '__main__':
    s = input()
    list(s)
    alnum=0
    alp=0
    dig=0
    low=0
    upp=0
    for i in s:
        if i.isalnum():
            alnum=1
        if i.isalpha():
            alp=1
        if i.isdigit():
            dig=1
        if i.islower():
            low=1
        if i.isupper():
            upp=1
    print(bool(alnum),bool(alp),bool(dig),bool(low),bool(upp),sep="\n")
