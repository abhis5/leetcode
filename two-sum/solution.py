class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(0, len(nums)):
            num = nums[i]
            if (num in dictionary):
                return [dictionary[num], i]
            dictionary[target - num] = i
        return []
