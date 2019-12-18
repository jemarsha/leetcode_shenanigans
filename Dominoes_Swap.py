#In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.
# (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
#We may rotate the i-th domino, so that A[i] and B[i] swap values.
#Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.
#If it cannot be done, return -1.
from collections import Counter
def dominoe_swap(arr1,arr2):

    if arr1==arr2:
        return 0

    if len(arr1) and len(arr2) <=1:
        return 0

    if len(arr1) == 0 or len(arr2) ==0:
        return -1

    a_count = Counter(arr1).most_common(1)[0]
    b_count = Counter(arr2).most_common(1)[0]
    count = 0

    highest_count_freq = max(a_count,b_count, key=lambda x:x[1])

    if a_count == highest_count_freq:
        chosen = arr1
        not_chosen= arr2

    else:
        chosen = arr2
        not_chosen = arr1

    highest = max(a_count, b_count, key=lambda x: x[1])[0]

    for i in range(len(chosen)):

        if not_chosen[i] is not None:
            if chosen[i] != highest:
                if not_chosen[i] == highest:
                    chosen[i], not_chosen[i] = not_chosen[i], chosen[i]
                    count+=1

                else:
                    return -1
            else:
                continue
        #return -1
    return count
if __name__ == '__main__':
    #O(n)

    A = [2,1,2,4,2,2]
    B = [5,2,6,2,3,2]

    a=[2, 1, 1, 1, 2, 2, 2, 1, 1, 2]
    b=[1, 1, 2, 1, 1, 1, 1, 2, 1, 1]
    print(dominoe_swap(a,b))

