list_number = [52,273,32,72,100]

try:
    number_input = int(input("정수입력"))
    print("{}번째 요소".format(number_input, list_number[number_input]))
except ValueError as exception:
    print("정수를 입력해주세요!")
    print(type(exception), exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어 났어요")
    print(type(exception), exception)
except Exception as exception:
    print("미리 파악 못한 에러가 발생 했습니다.")
    print(type(exception), exception)