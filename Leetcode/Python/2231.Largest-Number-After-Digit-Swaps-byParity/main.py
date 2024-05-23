class Solution:
    def largestInteger(self, num: int) -> int:

        def even_or_odd(n):
            if int(n) % 2 == 0:
                return "even" 
            else:
                return "odd" 
        num_list = list(str(num))
        for i in range(len(num_list)):
            for y in range(len(num_list)):
                if int(num_list[i]) > int(num_list[y]):
                    if even_or_odd(num_list[i]) == even_or_odd(num_list[y]):
                        n1 = num_list[i]
                        n2 = num_list[y]
                        num_list[i] = n2
                        num_list[y] = n1
        num_str = "" 
        return int(num_str.join(num_list))
