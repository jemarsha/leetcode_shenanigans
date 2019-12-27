def missing(temp):
    return sum(range(len(temp) + 1)) - sum(temp)



if __name__ == '__main__':
    temp = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(temp)
    print(missing(temp))