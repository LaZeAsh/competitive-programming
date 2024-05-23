import sys
# data = sys.stdin.read()
data = [5]
middle_point = data[0] / 2 + 1
for i in range(data[0]):
    print("*" * ((i - 1) * 2 + 1))
    if i == int(middle_point) - 1:
       print("*" * (data[0] * 2))
       print(" ")
       continue
    if (i != data[0] - 1):
        print(" ") # So doesn't leave whitespace after the bow-tie is finished
