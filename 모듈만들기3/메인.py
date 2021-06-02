import 모듈만들기 as test

if __name__ == "__main__":
    print("#메인의 __name__ 출력하기")
    radius = test.number_input()
    print(test.get_circumference(radius))
    print(test.get_circle_area(radius))