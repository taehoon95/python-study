#리스트 를 enumerate 이용하면 index를 키로 사용
example_list = ["요소A", "요소B", "요소C"]

for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i,value))

#딕셔너리 아이템
example_dictionary = {
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C"
}

print()
print("items() : ", example_dictionary.items())

for key, element in example_dictionary.items():
    print("dictinoary[{}] = {}".format(key, element))

#리스트 내포
print("\n리스트 내포 전")
array = []

#0~20까지 2의배수를 구한후 제곱
for i in range(0, 20, 2):
    array.append(i*i)

print(array)

print("\n리스트 내포")
array = []
array = [i*i for i in range(0,20,2)]
print(array)

array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]
print(output)