class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        prod = 1
        zc = 0
        for i in nums:
            if i == 0:
                zc = zc+1
                continue
            prod = prod*i
        if zc > 1:
            return ans
        if zc > 0:
            for i in range(len(nums)):
                if nums[i] == 0:
                    ans[i] = prod
            return ans
        for i in range(len(nums)):
            ans[i] = int(prod/nums[i])
        return ans