import sys
# data = sys.stdin.read().split(' ')
data = ["2", "3"]
data[0] = float(data[0])
data[1] = float(data[1])
if data[0]**2 > 3.14 * (data[1]**2):
    print("SQUARE")
else: 
    print("CIRCLE")

