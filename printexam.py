print("#하나만 출력1")
print()
print("#하나만 출력2 ", "abcd" ,sep="\n", end="\n\n")
print(type("#하나만 출력2 "), type(1),"abcd" ,sep="\n", end="\n\n")
print("결과")

print("안녕하세요"[0])
print("안녕하세요"[-3])
print("안녕하세요"[0:4])
print("안녕하세요"[3:])

hello = "안녕하세요"
print(type(hello), hello[:2], hello, sep="\n" , end="\n\n")
print(len(hello))

print(7//3)
print(4//3)

# res = input("인사말을 입력하세요>")
#print("입력한 인사말은 ", res)

a="a 10 20 30 40 50 ㅁ".split(" ")
print(type(a), a, sep="\n")

x, y, z = 10, 20, 30
print(x, y, z, sep='\n')

x, y = y, x
print(x, y , sep='\n')

