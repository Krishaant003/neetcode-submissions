class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = sorted(set(nums))
        if len(num) == 1:
            return 1
        print(num)
        curr = 1
        ans = 0
        prev = -100
        for i in num:
            if prev+1 == i:
                curr += 1
            else:
                curr = 1
            prev = i
            ans = max(ans,curr)
            
            
        return ans