print("{:b}".format(10))
print("{:o}".format(10))
print("{:x}".format(20))

print(int("1010",2))
print()
print(int(12),8)
print(int(10),16)

output = [i for i in range(1,100+1)
          if "{:b}".format(i).count("0") == 1]

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계: ", sum(output))