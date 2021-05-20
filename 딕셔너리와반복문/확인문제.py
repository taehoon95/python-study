
# #3

numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter={}
for number in numbers:
    if(number in counter):
        counter[number] = counter[number]+1
    else:
        counter[number] = 1

print(counter)

#4
character = {
    "name":"기사",
    "level":"12",
    "items":{
        "sword":"불꽃의 검",
        "armor":"풀플레이트"
    },
    "skill":["베기","세게 베기","아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:
        for small_key in character[key]:
            print(small_key, ":", character[key][small_key])
    elif type(character[key] is list):
        for item in character[key]:
            print(key, ":", item)
    else:
        print(key, ":", character[key])
