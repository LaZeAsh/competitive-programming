import math

num_inputs = int(input())
num_good_nums = 0

def check_if_num_prime(input_num):
    if input_num == 1:
        return False
    for x in range(2, int(math.sqrt(input_num) + 1)):
        if(input_num % x == 0):
            return False
    
    return True

for i in range(num_inputs):
    num = int(input())

    if not check_if_num_prime(num):
        continue 
    
    sum_nums = 0
    while (num / 10) > 0 or (num % 10) > 0:
        sum_nums += num % 10
        num = int(num / 10)

    if check_if_num_prime(int(sum_nums)):
        num_good_nums += 1
    
print(num_good_nums)
