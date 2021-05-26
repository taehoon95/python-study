list_a = [[10,20],[30,40,70,110],[50,60],[80,90,100]]
dict_a = {'k' : {'a':10, 'b':20}, 'l':{'a':10,'b':20,'c':40},'m':{'a':10}}


for i in dict_a:
    print(i, " => ",end='')
    for j in dict_a[i]:
        print("{} : {} ".format(j,dict_a[i][j]),end=' ')
    print()

print()

for i in list_a:
    print()
    for j in i:
        print(j,end=' ')
