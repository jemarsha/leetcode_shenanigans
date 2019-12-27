"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.
"""

def longest_conse_slow(arr):  #nlogn solution

    arr= sorted(arr)
    li =[]
    max_sequence= 0
    count = 1
    i=0
    while i+1 < len(arr):
        if arr[i]+1 == arr[i+1]:
            count += 1

            if max_sequence < count:
                max_sequence = count

        else:
            count = 1
        i+=1
    return max_sequence

def longest_conse_fast(arr):  #O(n) solution using a set with constant lookup time

    if len(arr) ==0:
        return 0

    if len(arr) ==1:
        return 1

    arr= set(arr)

    li =[]
    max_sequence= 0
    count = 1
    i=0
    for i in arr:
        if i-1 not in arr:

            num= i
            count = 1

        while num+1 in arr:

            num+=1
            count+=1

            max_sequence= max(max_sequence, count) #same as if count > max_sequence: max_sequence= count

        #if count > max_sequence:
            #max_sequence= count
    return max_sequence


if __name__ == '__main__':

    array = [100,101,102,103,104, 4, 200, 1, 3, 2]
    #array= [1]
    print(longest_conse_slow(array))
    print(longest_conse_fast(array))




