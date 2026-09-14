class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        print(Counter(nums).most_common(k))
        return [num for num, aaa in Counter(nums).most_common(k)]