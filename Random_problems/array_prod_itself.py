#Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].




def prod_arr_itself(arr):
    output = []

    length= len(arr)

    # fill a separate output array with 0s
    output = [0] * length

    #need to fill the first value with zero since no item to left of first item
    output[0] = 1

    for i in range(1, length):
        #this gets elements to the left of chosen element
        #start at 1 since output[0] is already filled,
        # then loop and multiply the value of prior
        # element in regular array and value of prior element in output array
        output[i] = arr[i-1] * output[i-1]


    #use this variable as a storage variable for the elements to the right of the chosen element
    r=1

    for i in reversed(range(length)):
        #loop through to get all elements on right side of the number and multiply the output

        output[i]= output[i] * r
        #multiply the numbers in original array together as you move along
        r *= arr[i]


    return output



if __name__ == '__main__':
    examp= [1,2,3,4]

    print(prod_arr_itself(examp))