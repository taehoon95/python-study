#1
print("#1\n")
def f(x):
    return x

print(f(10))

def f(x):
    return 2*x+1

print(f(10))

def f(x):
    return x*x + 2*x +1

print(f(10))

print("\n#2\n")

def mul(*values):
    output = 1
    for value in values:
        output = output * value
    return output

print(mul(5,7,9,10))