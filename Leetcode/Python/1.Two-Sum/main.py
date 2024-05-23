def twoSum(nums: List[int], target: int) -> List[int]:
    for num in nums:
        look = target - num
        if look in nums:
            return [num, look]