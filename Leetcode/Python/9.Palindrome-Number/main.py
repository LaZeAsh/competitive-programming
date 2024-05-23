class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x >= 0 and x <= 9:
            return True
        numStr = str(x)
        iteration = 1
        for val in numStr:
            if val == numStr[len(numStr) - iteration]:
                iteration += 1
                continue
            else:
                return False
        return True

# testClass = Solution() 

# print(testClass.isPalindrome(121)) 