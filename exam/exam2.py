# def solution(array, commands):
#     answer = []
#     save = []
#     for i in array:
#         save.append(i)
#     save = save[2-1:5]
#     save.sort()
#     print(save[2])
#     return answer

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a = commands[i][0]-1
        b = commands[i][1]
        c = commands[i][2]-1
        list = array[a:b]
        list.sort()
        answer.append(list[c])
    return answer

def solution2(array, commands):
    return[sorted(array[a-1:b])[c-1] for a, b, c in commands]


if __name__ == "__main__":
    array = [1,5,2,6,3,7,4]
    commands = [[2,5,3],[4,4,1],[1,7,3]]
    result = solution2(array, commands)
    print(type(result),result)

