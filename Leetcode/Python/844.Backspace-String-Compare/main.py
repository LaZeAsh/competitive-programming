class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        if "#" in s or "#" in t:
            print(s)
            print(t)
            while "#" in s or "#" in t:
                s_index = s.find("#")
                t_index = t.find("#")
                if s_index != -1:
                    if s_index >= 1:
                            replacement = s[(s_index - 1):(s_index + 1)]
                            s = s.replace(replacement, "", 1)
                    if s_index == 0:
                        s = s.replace("#", "", 1)
                if t_index != -1:
                    if t_index >= 1:
                        replacement = t[(t_index - 1):(t_index + 1)]
                        t = t.replace(replacement, "", 1)
                    if t_index == 0:
                       t = t.replace("#", "", 1) 
        else:
            if s != t:
                return False 
        if s != t:
            return False
        else:
            return True
testClass = Solution()
print(testClass.backspaceCompare("a##c", "#a#c"))