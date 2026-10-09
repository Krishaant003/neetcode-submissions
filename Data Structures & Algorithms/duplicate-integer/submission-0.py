class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test = set(nums)
        return not(len(nums) == len(test))
        