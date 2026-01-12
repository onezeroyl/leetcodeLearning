from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        while 0 in nums:
            nums.remove(0)
            count += 1
        for _ in range(count):
            nums.append(0)

    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return
        zero_index = nums.index(0)
        for index in range(zero_index + 1, len(nums)):
            if nums[index] != 0:
                nums[index], nums[zero_index] = nums[zero_index], nums[index]
                zero_index = zero_index + 1

solution = Solution()
nums = [1,2,3,4,5]
solution.moveZeroes2(nums)
print(nums)






