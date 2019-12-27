def binary_search(arr,target):

    if len(arr) ==0:
        return "Not Found"

    mid = len(arr)//2

    if arr[mid] == target:
        return "Found"

    # because you're returning a new array this function must return instead of just being called. Same as before.

    else:
        if arr[mid] > target:

            return binary_search(arr[:mid], target)

        else:

            return binary_search(arr[mid+1:], target)


    return False

if __name__ == '__main__':

    example = [1,7,9,32,39]
    print(binary_search(example,5))



