class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        opentoclose={"(":")","[":"]","{":"}"}
        for n in s:
            if n in opentoclose:
                if stack and stack[-1]==opentoclose[n]:
                    stack.append(n)
                else:
                    stack.pop(n)
            else:
                return True

        return False if not stack else True
