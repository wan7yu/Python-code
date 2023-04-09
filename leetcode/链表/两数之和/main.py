"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            j = i+1
            while j <= len(nums)-1:
                if nums[i] + nums[j] == target:
                    nums[:] = [i, j]
                j += 1
        return nums

# def twoSum(nums: list[int], target: int) -> list[int]:
#     for i in range(len(nums)-1):
#         j = i+1
#         while j <= len(nums)-1:
#             if nums[i] + nums[j] == target:
#                 nums[:] = [i, j]
#             j += 1
#         return nums


# def create_list() -> list[int]:
#     x = input("请输入列表中元素,逗号分隔:")
#     lis = x.split(',')
#     for i in range(len(lis)):
#         lis[i] = int(lis[i])
#     return lis


# num1 = create_list()
# print("the list is:", num1)
# target = int(input("请输入一个目标数:"))
# print(twoSum(num1, target))
