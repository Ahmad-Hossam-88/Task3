class Solution:
    def rob(self, nums: list[int]) -> int:
        current1, current2 = 0, 0
        for i in nums:
            hold = max(i + current1, current2)
            current1 = current2
            current2 = hold
        return current2
