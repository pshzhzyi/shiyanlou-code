a = 1
while a <= 100:
    if a % 7 != 0:
        l = list(str(a))
        # print(l,end=" ")
        if '7' not in l:
            # print('7' not in l)
            print(a)

    a=a+1


