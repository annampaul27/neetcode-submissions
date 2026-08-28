class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        a = sorted(nums)
        longest = 1
        current = 1
        for i in range(1, len(a)):
            if a[i] == a[i - 1]:
                continue  # skip duplicates
            if a[i] == a[i - 1] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1
        return max(longest, current)
        