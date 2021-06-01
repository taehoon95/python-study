import os
import sys

print("현재 운영체제: ", os.name)
print("현재 폴더: ", os.getcwd())
print("현재 폴더의 내부 요소: ", os.listdir())

if not os.path.exists("hello"):
    os.mkdir("hello")
if os.path.exists("hello"):
    os.rmdir("hello")

#파일을 생성하고 + 파일 이름을 변경합니다.
with open("orginal.txt", "w") as file:
    file.write("hello")

os.rename("orginal.txt", "new.txt")

std_list = [
   [1, "김상건", 90,80,70],
   [2, "이나연", 20,40,40],
]

if not os.path.exists("std_list.txt"):
    # if os.path.isfile("std_list.txt"):
        with open("std_list.txt", "w",encoding="utf-8") as f:
            for std in std_list:
                format_str = "{},{},{},{},{}\n".format(std[0],std[1],std[2],std[3],std[4])
                print(std)
                f.write(format_str)

std_list2 = []


with open("std_list.txt", "r", encoding="utf-8") as f:
    for line in f:
        std = line.strip().split(",")
        print("std : ", std, type(std))
        std = int(std[0]), std[1], int(std[2]), int(std[3]), int(std[4])
        #투플에서 리스트로 바꿔줄떄는 list()
        std_list2.append(list(std))


print("파일로 읽어들인 std_list2[] ", std_list2)

os.system("dir")
sys.exit()