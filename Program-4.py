
#Counting the multiples and adding into dictonary

def countmultiple(values_list):
    dict_vaules = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for i in range(9):
        for j in values_list:
            if j % (i+1) == 0:
                dict_vaules[i+1]+=1
    return dict_vaules
values_list = [int(i) for i in input('Enter intergers with spaces like 1 2 3 ... ').split()]
print(countmultiple(values_list))
