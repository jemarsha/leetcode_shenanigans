a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0

c = a & b;        # 12 = 0000 1100   #and the bits
print ("Line 1 - Value of c is ", c)

c = a | b;        # 61 = 0011 1101  # just or
print ("Line 2 - Value of c is ", c)

c = a ^ b;        # 49 = 0011 0001   exclusive or
print ("Line 3 - Value of c is ", c)

c = ~a;           # -61 = 1100 0011   flip the bits. Also used to turn postiive number into negative since the last bit is being flipped
print("Line 4 - Value of c is ", c)

c = a << 2;       # 240 = 1111 0000   this shifts all bits in 'a' by two places to the left
print ("Line 5 - Value of c is ", c)

c = a >> 2;       # 15 = 0000 1111  this shifts all bits in 'a' by two places to the right
print ("Line 6 - Value of c is ", c)

t= '1010'
b= '1001'

print(bin(int(t,2)+ int(b,2)))  #add two binary numbers the 2 just means the base. Bin converts from decimal to binary