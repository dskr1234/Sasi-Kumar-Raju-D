
#Number printing series


def numberseries(a):
    if a % 2 == 0:
        series=[]
        b=1
        for i in range((a//2) + 1):
            series.append(str(b))
            b+=2
        return ",".join(series)
    else:
        series=[]
        b=1
        for i in range(((a+1)//2) + 1):
            series.append(str(b))
            b+=2
        return ",".join(series)

a=int(input('Enter your range of printing series: '))
print(numberseries(a))


