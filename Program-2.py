
#Odd series printing

def oddseries(a):
    series=[]
    b=1
    for i in range(a):
        series.append(str(b))
        b+=2
    return ",".join(series)
a=int(input('Enter your range of printing series: '))
print(oddseries(a))
