"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
"""


def searchInsert(nums: list[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    bigger = False
    lower = False
    for num in nums:
        if target > num:
            bigger = True

        if target < num:
            lower = True

        if bigger and lower:
            return nums.index(num)
    if max(nums) < target:
        return len(nums)
    if min(nums) > target:
        return 0


print(searchInsert([1, 3, 5, 6], 5))
print(searchInsert([1, 3, 5, 6], 2))
print(searchInsert([1, 3, 5, 6], 7))
print(searchInsert([1, 3, 5, 6], 0))
