#반복문과 범위의 조합 range

for i in range(0,10,3):
    print(str(i) + "=반복 변수")
print()

#몇 번 반복인지를 알아야 하는 경우
array = [273, 32, 103, 57, 52]
for i in range(len(array)):
    print("{}번째 반복: {}".format(i,array[i]))
print()

#역반복문 큰숫자에서 작은 숫자로 반복문 적용
for i in range(4,0-1,-1):
    print("현재 반복 변수: {}".format(i))
print()

for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))
