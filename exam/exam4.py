import os.path


def show_menu():
    result = 1
    try:
        result = int(input("1. 학생목록, 2. 학생 추가, 3. 학생 수정, 4. 학생 삭제, 5. 종료 [1-5] 번호를 입력하세요."))
    except ValueError as e:
        print("숫자 [1-5]값만 가능")
    finally:
        return result


def std_list_read_file():
    if os.path.isfile(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f:
                std = line.strip().split(",")
                std_list.append(std)


def std_list_write_file():
    if os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8") as f:
            for std in std_list:
                format_std = "{},{},{},{},{}\n".format(std[0], std[1], std[2], std[3], std[4])
                f.write(format_std)


def show_std_list():
    print("{:3} {:4} {:3} {:3} {:3} {:4} {:>4}".format('번호', '성명', '국어', '영어', '수학', '총점', '평균'))
    for std in std_list:
        total = int(std[2]) + int(std[3]) + int(std[4])
        avg = total / 3
        std_info = "{:3d} {:5} {:3d}  {:3d}  {:3d} {:4d} {:7.2f}".format(int(std[0]), std[1], int(std[2]), int(std[3]),
                                                                         int(std[4]), total, avg)
        print(std_info)


#
def add_std_info():
    res = [str(len(std_list)+1)]
    res.extend(get_std_info('성명,국어,영어,수학을 입력하세요 es)최영민 90 90 90'))
    if len(res) == 5:
        std_list.append(res)
    else:
        print("입력방식이 다릅니다.")
        return


# 구현하세요

def get_std_info(msg):
    result = input(msg)
    std_info = result.split(" ")
    return std_info


def update_std_info():
    update_num = input("수정번호입력 >>")
    for std in std_list:
        if std[0] == update_num:
            res = get_std_info('수정할 국어,영어,수학 입력 ex)90 90 90>>')
            if len(res) == 3:
                del std[2:5]
                std.extend(res)
                return
            else:
                print("입력방식이 다릅니다.")
                return
    print("없는 번호입니다.")


def delete_std_info():
    del_num = input("삭제번호입력")
    for std in std_list:
        if std[0] == del_num:
            std_list.remove(std)
            return
    print("없는 번호입니다.")


if __name__ == "__main__":
    std_list = []
    file_name = "std_list.txt"

    std_list_read_file()
    while True:
        res = show_menu()
        if res == 1:
            show_std_list()
        elif res == 2:
            add_std_info()
        elif res == 3:
            update_std_info()
        elif res == 4:
            print("학생 삭제")
            delete_std_info()
        else:
            std_list_write_file()
            break;
    print("프로그램 종료")