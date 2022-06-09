from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in nums[i + 1:]:
                return [i, nums[i + 1:].index(complement) + i + 1]


p1 = Solution()
print(p1.twoSum([2,7,11,15], 9))    # Expected output: [0,1]
print(p1.twoSum([3,2,4], 6))        # Expected output: [1,2]
print(p1.twoSum([3,3], 6))          # Expected output: [0,1]