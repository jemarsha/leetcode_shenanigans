def list_first(lst):  #return  the first unique one which would be
    long = []

    for i in range(len(lst)):  # dont do minus one unless you don't need the last element in the list
        if lst[i] in long:
            long.remove(lst[i])
        else:
            long.append(lst[i])
    return long[0]



if __name__ ==  '__main__':


    listi = ['two', 'one', 'two', 'one', 'three']
    print(list_first(listi))