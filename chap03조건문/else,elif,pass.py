number = input("정수를 입력하세요 > ")
number = int(number)

if number % 2 == 0 :
    print("짝수입니다.")
else:
    print("홀수 입니다.")

import datetime
now = datetime.datetime.now()
month = now.month

if 3 <= month <=5 :
    print("현재는 봄 입니다.")
elif 6 <= month <= 9:
    print("현재는 여름 입니다.")
elif 9 <= month <= 11:
    print("현재는 가을 입니다.")
elif 12 <= month <= 2:
    print("현재는 겨울 입니다.")
    
score = float(input("학점을 입력하세요 > "))

if score == 4.5:
    print("신")
elif 4.2 <= score:
    print("교수님의 사랑")
elif 3.5 <= score:
    print("현 체제의 수호자")
elif 2.8 <= score:
    print("일반인")
elif 2.3 <= score:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score:
    print("오락문화의 선구자")
elif 1.0 <= score:
    print("불가촉천민")
elif 0.5 <= score:
    print("자벌레")
elif 0 < score:
    print("플랑크톤")
else:
    print("시대를 앞서가는 혁명의 씨앗")

number = int(input("정수 입력 > "))

if number > 0:
    pass
else:
    pass


if number > 0:
    raise NotImplementedError
else:
    raise NotImplementedError

