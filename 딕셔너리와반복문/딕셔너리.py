
#딕셔너리를 선언합니다.
dictionary={
    "name":"7D 건조 망고",
    "type":"당절임",
    "ingredient":["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin":"필리핀"
}

#출력합니다.
print("출력")
print(dictionary)
print("name: ",dictionary["name"])
print("type: ",dictionary["type"])
print("ingredient: ",dictionary["ingredient"])
print("origin: ",dictionary["origin"],"\n")

#값을 변경합니다.
print("딕셔너리 name값 변경")
dictionary["name"] = "8D 건조 망고"
print("name: ",dictionary["name"],'\n')

print("dictionary[ingredient]안의 값 반복문으로 출력")
for e in dictionary["ingredient"]:
    print("ingredient - " ,e)

#nameerror오류
name = "이름"
dict_key = {
    name:"7D 건조 망고",
    type:"당절임"
}

print(dict_key)

dictionary["price"] = 5000
print(dictionary)

dictionary["price"] = 1500
print(dictionary)

del dictionary["price"]
print(dictionary)

key = input("> 접근하고자 하는 키")
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")

value = dictionary.get(key)
print("값 ",value)

if value == None:
    print("존재하지 않는 키에 접근하고 있습니다.")

print("딕셔너리 반복문\n\n")
for key in dictionary:
    print(key, ":" , dictionary[key])