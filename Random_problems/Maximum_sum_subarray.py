import math

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def get_max_sum(arr):
    if len(arr) == 0:
        return
    meh = -math.inf
    msf = -math.inf
    for i in range(len(arr)):
        meh = meh + arr[i]

        if meh < arr[i]:
            meh = arr[i]

        if msf < meh:
            msf = meh
    return msf