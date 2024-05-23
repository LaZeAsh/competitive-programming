class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        fizz_list = list()
        for i in range(n):
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                fizz_list.append("FizzBuzz") 
                continue
            if (i + 1) % 3 == 0:
               fizz_list.append("Fizz")
               continue
            if (i + 1) % 5 == 0:
                fizz_list.append("Buzz") 
                continue
            fizz_list.append(str(i + 1))
        return fizz_list