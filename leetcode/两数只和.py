from ast import List



class Solution:
    # 暴力破解法，时间复杂度O(n2)
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for index1 in range(len(nums)):
            a = nums[index1]
            for index2 in range(index1 + 1, len(nums)):
                b = nums[index2]
                if a + b == target:
                    return [index1, index2]
        return []
    # 哈希表优化解法 时间复杂度O(n)
    def two_sum_by_hash(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            part = target - num
            if part in dict:
                return [dict[part], i]
            dict[num] = i
        return []


sl = Solution()
print(sl.two_sum_by_hash([2,7,11,15], 9))



