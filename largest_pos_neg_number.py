def largest_neg_pos(nums): #O(n)

    l_neg = float("-inf")
    l_pos = 0

    for i in range(len(nums)):
        print(i)
        if nums[i] <0:
            if nums[i] > l_neg:
                l_neg = nums[i]
        else:
            if nums[i] > l_pos:
                l_pos = nums[i]

    return l_neg, l_pos


if __name__ == '__main__':

    numbers = [-5,4,-30,1,3,20]

    print(largest_neg_pos(numbers))