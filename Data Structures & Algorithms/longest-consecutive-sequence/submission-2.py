class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxi=0
        lis=set(nums)
        for num in lis:
            count=1
            if num-1 in lis:
                continue
            while num+count in lis:
                count+=1
            maxi=max(maxi,count)
        return maxi