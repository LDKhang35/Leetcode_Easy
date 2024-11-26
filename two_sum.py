class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idex = {}
        for i, num in enumerate(nums):
            if target - num in pair_idex:
                return [i, pair_idex[target - num]]
            pair_idex[num] = i