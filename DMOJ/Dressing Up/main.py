import ast
import sys
# data = sys.stdin.read().split(' ')
data = [5]
# print(int(data[0] / 2))
# data = ["2", "3"]

data[0] = int(data[0])
middle_point = int(data[0] / 2) + 1 # Gets the mid point by truncating the number and adding 1
last_point = data[0] * 2
astericks = "*"
# We are always getting an odd number
for i in range(data[0] + 1):
    # print(str(middle_point) + " " + str(i))
    # Printing the astericks for beginning of bow tie
    # if i == middle_point:
    #     print("*" * last_point)
    #     # astericks = "*" * (len(astericks) - 2)
    #     i += 1
    #     continue # Rest of the loop won't be executed
    # Printing Astericks
    if i != 0:
        print(astericks, end="")
        print(" " * (last_point - (len(astericks) * 2)), end="")
        print(astericks)

    if i < middle_point:
        astericks += "**"
    if i > middle_point:
        # print("Decreasing astericks!")
        astericks = "*" * (len(astericks) - 2)