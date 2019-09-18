class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from collections import defaultdict

        length = len(nums)

        # sanity check
        if length < 3:
            return []

        nums = sorted(nums)
        triples = []
        triples_sets = defaultdict(set)
        for i in range(length):
            left = i + 1
            right = length - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    if (
                        nums[i] in triples_sets
                        and nums[left] in triples_sets[nums[i]]
                    ):
                        left += 1
                        right -= 1
                        continue
                    triples.append([nums[i], nums[left], nums[right]])
                    triples_sets[nums[i]].add(nums[left])
                    left += 1
                    right -= 1
        return triples
