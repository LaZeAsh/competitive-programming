class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = list(s)
        t_list = list(t)
        dict_key = {} 
        for i in range(len(s)):
            if s_list[i] in dict_key and dict_key.get(s_list[i]) != t_list[i]:
                return False
            if t_list[i] in dict_key.values() and   s_list[list(dict_key.values()).index(t_list[i])] != s_list[i]:
                return False
            dict_key.update({s_list[i] : t_list[i]})
        return True 
