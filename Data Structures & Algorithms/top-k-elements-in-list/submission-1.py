class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums).most_common(k)
        res = []
        for key, val in count:
            res.append(key)
        
        return res