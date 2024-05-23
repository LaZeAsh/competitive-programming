class Solution:
    # def canPlaceFlowers(self, flowerbed, n) -> bool:
    def canPlaceFlowers(self, flowerbed, n) -> bool:
        inBetween = False
        if flowerbed[0] == 1:
            inBetween = True
        if len(flowerbed) <= 2:
            if flowerbed[0] == 1:
                return 0 >= n
            else:
                return 1 >= n
        flowerbed = [0] + flowerbed + [0]
        num_gaps = 0
        max_new_flowers = 0
        for i in range(1, len(flowerbed)):
            if flowerbed[i] == 1:
                if num_gaps > 0:
                    if not inBetween:
                        max_new_flowers += (num_gaps) // 2
                    else:
                        max_new_flowers += (num_gaps - 1) // 2
                    if not inBetween:
                        inBetween = True
                num_gaps = 0
            else:
                num_gaps += 1
        if num_gaps > 0:
            if not inBetween:
                max_new_flowers += (num_gaps) // 2
            else:
                max_new_flowers += (num_gaps - 1) // 2

        # Return True if the number of new flowers that can be planted is at least n
        return max_new_flowers >= n

sol = Solution()
print(sol.canPlaceFlowers([0, 0, 0], 2))

# The logic is incorrect