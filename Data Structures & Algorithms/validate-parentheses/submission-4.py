class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        opentoclose={"(":")","[":"]","{":"}"}
        for n in s:
            if n in opentoclose:
                if stack and stack[-1]==opentoclose[n]:
                    stack.append()
                else:
                    return True
            else:
                stack.pop("opentoclose")

        return False if not stack else True
