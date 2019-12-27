def extractKBits(num, k, p):
    # convert number into binary first
    binary = bin(num)
    print(binary)
    # remove first two characters
    binary = binary[2:]
    print(binary)
    end = len(binary) - p #subtract the positions from the length of the binary after removing 0b from beginning
    print(len(binary) - p)
    start = end - k + 1  #subtract the k bits
    print(start)

    # extract k  bit sub-string
    kBitSubStr = binary[start: end + 1]
    print(kBitSubStr)
    # convert extracted sub-string into decimal again
    print(int(kBitSubStr, 2))


# Driver program
if __name__ == "__main__":
    num = 171
    k = 5
    p = 2
    extractKBits(num, k, p)


    #10101011
#06408021