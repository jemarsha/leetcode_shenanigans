# Zipped Function
"""
Returns an iterator of tuples, where the i-th tuple contains the i-th element
from each of the argument sequences or iterables.
The iterator stops when the shortest input iterable is exhausted.
With a single iterable argument, it returns an iterator of 1-tuples.
With no arguments, it returns an empty iterator.
"""


from typing import List

global N

board = [[0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0],
         [0, 0, 0, 0, 3],
         [0, 0, 0, 1, 0]]
row = len(board)
col = len(board[0])
N = 4
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j])


# LOOP IN PARALLEL TO GET DIAGNOL
for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
    pass

# If you’re working with sequences like lists, tuples, or strings,
# then your iterables are guaranteed to be evaluated from left to right.
# This means that the resulting list of tuples will take the form
# [(numbers[0], letters[0]), (numbers[1], letters[1]),..., (numbers[n], letters[n])]

#Don't use sets with zipped or the order won't match up

letters = ['a', 'b', 'c']
numbers = [5, 3, 1, 5, 6]
symbols: List[str]= ['%','.','-']
zipped = zip(letters, numbers,symbols)
# print(zipped)
print(list(zipped))

#Can Also use zip() to unzip tuples and elements as well with the unpacking operator *zip

tup = ((1,'a'), (2,'b'), (5,'d'))
nums,lets = zip(*tup)
print(list(zip(*tup)))  #same as printing nums and lets.  It just unzips the tuple
for i in list(zip(*tup)):
    if i[2] == 5:
        print(i[0])

def sum_zips(arr1,arr2):  #ALLOWS YOU TO do something to 2 lists in parallel

    for i,j in zip(arr1,arr2):
        profit = i-j
        print(profit)

sales = [50100, 52000, 60000]
losses = [30000, 22000, 11000]
sum_zips(sales,losses)

fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']

field = ['age']
value= ['52']
a_dict = dict(zip(fields,values))
a_dict.update(zip(field,value))

print(a_dict)




