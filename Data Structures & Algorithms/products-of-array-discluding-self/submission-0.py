class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)
        total = 1
        for num in nums:
            if num != 0:
                total *= num
        new = []
        for num in nums:
            if zero_count == 1:
                if num == 0:
                    new.append(total)
                else:
                    new.append(0)
            else:
                new.append(total // num)
        return new

        