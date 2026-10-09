class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = {}
        for i in nums:
            if i not in check:
                check[i] = 0
            check[i] = check[i]+1
        check_sorted =  dict(sorted(check.items(),key=lambda x: x[1], reverse=True))
        
        ans = []
        for i in check_sorted:
            if k == 0:
                break
            ans.append(i)
            k = k -1
        return ans