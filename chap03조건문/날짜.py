import datetime

#현재날짜
now = datetime.datetime.now()

#출력
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

print("{0}년 {0}월 {0}일 {0}시 {0}분 {5}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

if now.hour < 12:
    print("현재는 오전{}시 입니다.".format(now.hour))
if now.hour > 12:
    print("현재는 오후{}시 입니다.".format(now.hour))

if 3 <= now.month < 6:
    print("현재 계절은 {}월 봄입니다.".format(now.month))
if 6 <= now.month < 9:
    print("현재 계절은 {}월 여름입니다.".format(now.month))
if 9 <= now.month < 11:
    print("현재 계절은 {}월 가을입니다.".format(now.month))
if 11 <= now.month < 2:
    print("현재 계절은 {}월 겨울입니다.".format(now.month))

# last_number = input("정수 입력 > ")
# last_number = int(last_number)
#
# if last_number == 0 \
#     or last_number == 2\
#     or last_number == 4\
#     or last_number == 6\
#     or last_number == 8:
#     print("짝수입니다")
#
# if last_number == 1 \
#     or last_number == 3\
#     or last_number == 5\
#     or last_number == 7\
#     or last_number == 9:
#     print("홀수입니다")

# number = input("정수 입력 > ")
# last_number = number[-1]
#
# #짝수 조건
# if last_number in "02468":
#     print("짝수 입니다.")
#
# #홀수 조건
# if last_number in "13579":
#     print("홀수 입니다.")

number = input("정수 입력 > ")
number = int(number)

#짝수 조건
if number % 2 == 0:
    print("짝수 입니다.")

#홀수 조건
if number % 2 == 1:
    print("홀수 입니다.")

