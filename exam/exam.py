def dan(num):
    for i in range(2,10):
        print('{} * {} = {:2}'.format(i, num, num * i),end='\t')

def gugudan():
    for j in range(1,10):
        dan(j)
        print()

if __name__ == "__main__":
    gugudan()
