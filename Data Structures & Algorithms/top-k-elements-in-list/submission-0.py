from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fr = Counter(nums)
        sorted_element=sorted(fr.keys(),key=lambda x: fr[x], reverse=True)
        return sorted_element[:k]

        