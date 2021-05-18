array = [274,53,243,"문자열",True,False]
print(array)

list_a = [274,53,243,"문자열",True,False]
print(list_a[0])
print(list_a[0:2])
list_a[0]="변경"
print(list_a)
print(list_a[-6])
print(list_a[3][2])

list_a = [1 ,2 ,3]
list_b = [4 ,5 ,6]
print(list_a+list_b)
list_c = list_a+list_b

list_c.insert(4,100)
print(list_c)

list_c.extend(list_b)
print(list_c)

del list_c[4]
print(list_c)

list_c.pop(3)
print(list_c)

del list_c[5:7]
print(list_c)

del list_c[3:]
print(list_c)

list_c.remove(1)
print(list_c)

print(list_a)

print(6 not in list_a)


for ㅑ in range(11):
    print("출력")

array = [1 ,2 ,3, 4, 5]

for i in array:
    print(i)