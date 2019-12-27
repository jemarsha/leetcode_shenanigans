


def trapped(arr):

    # create 2 arrays left and right to keep track of the largest height of bars on either side of current element
    length = len(arr)

    if length <= 1:
        return 0
    left = [0] * length

    right = [0] * length

    #water variable to sum up the water at the end
    water = 0

    #first element of left is always first element
    left[0] = arr[0]

    #get max of values on left of element
    for i in range(1,length):
        left[i] = max(left[i-1],arr[i])

    #fill the end of the right array with the final value in the array
    right[length - 1] = arr[length - 1]

    #get max of values on right of element
    for i in range(length-2, -1, -1):

        right[i] = max(right[i+1], arr[i])

    #now get the amount of water by taking the min on either side of the element and subtracting that from the value of element
    for i in range(length):
        water += min(left[i], right[i]) - arr[i]

    return water
if __name__ == '__main__':

    memp = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trapped(memp))