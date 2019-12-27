#Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

#The update(i, val) function modifies nums by updating the element at index i to val.

#The array is only modifiable by the update function.
#You may assume the number of calls to update and sumRange function is distributed evenly.


class NumArray:

    def __init__(self, nums: List[int]):

        self.nums = nums

    def update(self, i: int, val: int) -> None:

        if len(self.nums) < 1:
            return

        else:
            self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:

        if len(self.nums) <= 1:
            return self.nums
        summation = 0
        for n in range(i, j + 1):
            summation += self.nums[n]
        return [summation]