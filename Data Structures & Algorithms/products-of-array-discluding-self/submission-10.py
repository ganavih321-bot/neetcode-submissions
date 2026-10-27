class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro=[]
        for i in range(len(nums)):
            pr=1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    pr *= nums[j]
            pro.append(pr)
        return pro