class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        left = n - 1
        for i in reversed(range(n - 1)):
            if i + nums[i] >= left:
                left = i
        return left == 0
