class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opens=close=0
        for c in s:
            if c=="(":
                opens+=1
            elif opens:
                opens-=1
            else:
                close+=1
        return close+opens
