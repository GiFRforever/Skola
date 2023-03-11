# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         # sort
#         numsd = nums.copy()
#         numsd.sort()
#         numsd = [n for n in numsd if n <= (target - numsd[0])]
#         for ind1, val1 in enumerate(numsd):
#             for val2 in numsd[(ind1 + 1) : :]:
#                 if (v := val1 + val2) == target:
#                     # find index of val1 and val2 in nums and return in list, on one line
#                     if val1 == val2:
#                         # find index of val1 and val2 in nums and return in list, on two lines, the indexes must not be the same
#                         return [
#                             nums.index(val1),
#                             nums.index(val2, nums.index(val1) + 1),
#                         ]
#                     return [nums.index(val1), nums.index(val2)]
#                 elif v > target:
#                     break
#         else:
#             return [0, 0]


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        checked = {}
        i = 0
        while target - nums[i] not in checked:
            checked[nums[i]] = i
            i += 1

        return [checked[target - nums[i]], i]


s = Solution()

# random test for twoSum
import random

bad = 0
for _ in range(1000):
    nums = [random.randint(0, 1000) for _ in range(random.randint(2, 100))]
    target = random.randint(0, 1000)
    e1 = random.randint(0, target)
    e2 = target - e1
    nums.insert(random.randint(0, len(nums)), e1)
    nums.insert(random.randint(0, len(nums)), e2)
    r = s.twoSum(nums, target)
    if r[0] == 0 and r[1] == 0:
        # print(nums, target, r)
        bad += 1
    else:
        if nums[r[0]] + nums[r[1]] != target:
            # print(nums, target, r)
            bad += 1
print(bad)
