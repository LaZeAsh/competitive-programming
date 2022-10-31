import sys
# data = ["5", "6", "7"]
data = sys.stdin.read().split('\n')
data[0] = int(data[0])
data[1] = int(data[1])
data[2] = int(data[2])

for i in range(data[0]):
    print("*", end="")
    print(" " * data[1], end="")
    print("*", end="")
    print(" " * data[1], end="")
    print("*")

times_to_print = data[1] * 2 + 3
print("*" * times_to_print, end="\n")

for x in range(data[2]):
    print(" " * (int(times_to_print / 2)), end="")
    print("*")

