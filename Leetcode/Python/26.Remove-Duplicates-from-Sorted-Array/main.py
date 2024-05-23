class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        next_index = 0
        already_accounted = -1
        for i in range(len(nums)):
            print(i)
            if i == (len(nums) - 1):
                if already_accounted == nums[i]:
                    next_index -= 1
                    break 
                nums[next_index] = nums[i] 
                continue
            if nums[i] == nums[i + 1]:
                if nums[i] == already_accounted:
                    continue
                nums[next_index] = nums[i]
                already_accounted = nums[i]
                next_index += 1
                continue
            if nums[i] == already_accounted:
                continue
            next_index += 1
            
        return (next_index + 1) 
            
testClass = Solution() 

print(testClass.removeDuplicates([1, 1, 2, 3]))