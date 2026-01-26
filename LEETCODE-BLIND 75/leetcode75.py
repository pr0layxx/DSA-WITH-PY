# QESTION NO: 121
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP


# obj = Solution()
# prices = [7, 1, 5, 3, 6, 4]
# result = obj.maxProfit(prices)

# print("Max Profit:", result)


# QUESTION NO: 217


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)
        return False


# obj = Solution()
# nums = [1, 2, 3, 1]

# result = obj.containsDuplicate(nums)
# print("Contains Duplicate:", result)


# QUESTION NO: 238


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

obj = Solution()


nums = [1, 2, 3, 4]

result = obj.productExceptSelf(nums)
print("Product Except Self:", result)
