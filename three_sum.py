from typing import List


def three_sum(nums): #n^3
    """Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.
    """
    temp = set()
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i]+nums[j] + nums[k] == 0:
                    temp.add(tuple(sorted([nums[i],nums[j],nums[k]])))
    print(temp)
    # can add tuple to set but not list

def three_sum_fast(nums): #n^2
    """Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.
    """
    temper = set()
    nums = sorted(nums)
    for i in range(len(nums)-1):

        x = nums[i]
        l = i+1
        r = len(nums)-1

        while l<r:

            if x + nums[l] + nums[r] == 0:
                temper.add(tuple([x, nums[l], nums[r]]))
                l+=1
                r -=1

            elif x + nums[l] + nums[r] < 0:
                l+=1

            else :
                r-=1
    print(temper)

if __name__ == '__main__':
    three_sum_list: List[int] = [-1, 0, 1, 2, -1, -4]

    three_sum_fast(three_sum_list)
