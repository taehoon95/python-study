#1~100까지 짝수만 list(even_list)에 저장하고 출력하시오.
even_list = [i for i in range(101) if i % 2 == 0]
print(even_list)

#1~100까지 홀수만 list(odd_list)에 저장하고 출력하시오.
odd_list = [i for i in range(101) if i % 2 != 0]
print(odd_list)


#2
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number > 100 :
        print("- 100이상의 수 : ", number)

#3

for number in numbers:
    if number % 2 == 0:
        print("{}짝수 입니다.".format(number))
    else:
        print("{}홀수 입니다.".format(number))

for number in numbers:
    if number % 10 == 1:
        print("{}는 한자리수 입니다.".format(number))
    elif number % 10 == 2:
        print("{}는 두자리수 입니다.".format(number))
    elif number % 10 == 3:
        print("{}는 세자리수 입니다.".format(number))


#4
list_of_lists = [
    [1,2,3],
    [4,5,6,7],
    [8,9]
]

for list_of_list in list_of_lists:
    for i in list_of_list:
        print(i)

list_seq = [i for sub_list in list_of_lists for i in sub_list]
print("list_seq ", i)
#5
print("5번")
numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

#for number in numbers:
    #output[].append(number)
print(output)