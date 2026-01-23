class Solution:
    def twoSum(self, nums, target):
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


# ---- Test / Print ----
nums = [2, 7, 11, 15]
target = 9

sol = Solution()
ans = sol.twoSum(nums, target)

print("Indexes:", ans)
print("Values:", nums[ans[0]], "+", nums[ans[1]], "=", target)