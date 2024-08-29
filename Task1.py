class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def check(piles, speed):
            sum = 0
            for i in piles:
                sum += math.ceil(i / speed)
            return sum

        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            if check(piles, mid) <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low