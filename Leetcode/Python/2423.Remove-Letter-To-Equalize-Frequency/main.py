class Solution:
    def equalFrequency(self, word: str) -> bool:

        freq = {}
        
        # count number of occurences of every letter
        for char in word:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        if len(freq) <= 2:
            return True
        # take values from dictonary
        values = list(freq.values())

        min_freq = min(values)
        max_freq = max(values)
        
        if min_freq == 1 and max_freq == 1:
            return True
        if max_freq - min_freq == 0: 
            return False
        elif max_freq - min_freq == 1:
            if values.count(min_freq) > 1 and values.count(max_freq) > 1:
                return False
            return True
        else:
            return False
         
        # if max_freq == min_freq:
        #     return False
        # if max_freq - min_freq > 1:
        #     return False
        # max_char = chr(freq.index(max_freq) + ord('a'))
        # new_word = ""
        # for i in range(n):
        #     if word[i] == max_char:
        #         freq[ord(max_char) - ord('a')] -= 1
        #         if freq[ord(max_char) - ord('a')] == 0:
        #             freq[ord(max_char) - ord('a')] = 100
        #         break
        #         # new_word = word[:i] + word[i+1:]
        
        # min_freq = min(freq)
        # for i in range(len(freq)):
        #     if freq[i] == 100:
        #         freq[i] = -1
        # max_freq = max(freq)
        
        # if max_freq - min_freq == 0:
        #     return True
            # if freq[ord(word[i]) - ord('a')] == min_freq:
            #     new_word = word[:i] + word[i+1:]
            #     new_freq = [0] * 26
            #     for j in range(len(new_word)):
            #         new_freq[ord(new_word[j]) - ord('a')] += 1
            #     if len(set(new_freq)) == 1:
            #         return True
            #     break
            # if word[i] == max_char:
            #     freq[ord(max_char) - ord('a')] += 1
        
        return False

sol = Solution()
sol.equalFrequency("aazz")

# The logic is incorrect 