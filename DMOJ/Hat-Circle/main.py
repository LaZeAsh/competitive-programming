import sys

N = int(sys.stdin.readline())
if N % 2 != 0:
    print(0)
    exit()
secondary_index = 0
idx = 0
arr = []

for i in range(N):
    H = int(sys.stdin.readline())
    arr.append(H)
    # Even number of people on the table
    if i >= (N/2):
        if arr[i] == arr[secondary_index]:
            idx += 2
        secondary_index += 1
print(idx)

