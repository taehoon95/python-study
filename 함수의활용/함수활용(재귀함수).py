def factorial(n):
    output = 1
    for i in range(1,n+1):
        output *= i
    return output

print("4! : " , factorial(4))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("5! : ", factorial(5))

def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("finonacci(6) : ",  fibonacci(6),"\n")

counter = 0
def fibonacci(n):
    print("fibonacci({})를 구합니다. ".format(n))
    global counter
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
fibonacci(5)
print("fibonacci(5) 계산에 활용된 덧셈횟수는 {}번 입니다. ".format(counter))

dictionary = {
    1: 1,
    2: 1
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output

print("\nfibonacci(10): ", fibonacci(10))
print("fibonacci(20): ", fibonacci(20))