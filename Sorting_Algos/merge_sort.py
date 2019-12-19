def merge_sort(arr):

    if len(arr) < 2:
        return arr
    #mid = len(arr)/2
    mid = len(arr) //2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])


    return merge(left,right)


def merge(l_arr,r_arr):
    if not len(l_arr) or not len(r_arr):
        return l_arr or r_arr


    result = []

    i=0
    j=0

    while len(result) < len(l_arr) + len(r_arr):
        if l_arr[i] < r_arr[j]:
            result.append(l_arr[i])
            i+=1

        else:

            result.append(r_arr[j])
            j+=1

        if i == len(l_arr) and j != len(r_arr):

            result.extend(r_arr[j:])
            #break

        elif j==len(r_arr) and i != len(l_arr):

            result.extend(l_arr[i:])
            #break

    return result


if __name__ == '__main__':

    arr = [2,5,1,8,4,2,3]
    print(merge_sort(arr))

