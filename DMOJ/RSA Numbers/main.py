import sys
data = sys.stdin.read().split('\n')
# data = ["5", "6"]
data[0] = int(data[0])
data[1] = int(data[1])
rsa_nums = 0
factors = 0
# For loop between the ranges of the number
for number in range(data[0], data[1] + 1):
    # print(number)
    # Figure out if a number is RSA
    # Every number has 2 factors (1 and number itself) 
    for divisor in range(1000):
        # print(divisor)
        if number % (divisor + 1) == 0:
            # print("Modulus!")
            factors += 1
    if factors == 4:
        # print("RSA Number!")
        rsa_nums += 1
    factors = 0
# Output
print("The number of RSA numbers between " + str(data[0])  + " and " + str(data[1]) + " is " + str(rsa_nums))