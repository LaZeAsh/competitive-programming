import sys
data = int(sys.stdin.read())

for i in range(int((len(data) - 1) / 2)):
    firstInt = data[i + 1]
    secondInt = data[i + 2]
    # print(" " * i, end="")
    print(secondInt + firstInt)
 