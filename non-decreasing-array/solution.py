class Solution:
    def checkPossibility(self, nums):
        p = None
        count = 0
        if 1 <= len(nums) <= 2:
            return True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if count >= 2:
                    return False
                p = i
        return (p is None or p is 0 or p is len(nums) - 2
               or (nums[p - 1] < nums[p] and nums[p + 1] < nums[p]))
