class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if i == (len(nums) - 1):
                return False
            if nums[i] == nums[i + 1]:
                return True
        return False