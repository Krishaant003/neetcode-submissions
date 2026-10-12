class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return  '0--'
        ans = "--".join(strs)
        return ans

    def decode(self, s: str) -> List[str]:
        print(s)
        if s == '0--':
            return []
        return s.split("--")
