class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        num_list = list(s)
        roman_map = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        prev_char = ""
        for val in num_list:
            if prev_char != "" and roman_map[prev_char] < roman_map[val]:
                value += roman_map[val] 
                value -= (roman_map[prev_char] * 2)
            else:
                value += roman_map[val]
                prev_char = val
        return value
                    
# testClass = Solution() 

# print(testClass.romanToInt("LVIII"))
