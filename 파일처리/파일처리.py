#바로 basic.txt 생성
def fopen1(filename):
    file = open(filename,"w")
    file.write("Hello JAVA Programing...!")
    file.close()


# with : close()자동으로 해준다
def fopen2(filename):
    with open(filename, "w") as f:
        f.write("HMM good")

#fopen1("basic3.txt")
#fopen2("basic4.txt")

# read
def f_read(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents


c = "basic3.txt"
d = f_read("basic4.txt")
print(f_read(c))
print(d)


