#from typing import List
class Node:

    def __init__(self,value):
        self.value = value

        self.next = None

def merge_lists(lists):

    """

    This function merges sorted linked lists- Reads the values in one at a time into a list O(kn). Then
    sorts them O(nlogn). Then puts them into a linked list (O(n). Overall complexity is O(kn). This can be improved


    @param lists: list of sorted linked lists
    @return: a sorted linked list
    """

    nodes = []
    head = point= Node(0)
    for val in lists:
        while val:
            nodes.append(val.value)

            val= val.next

    nodes = sorted(nodes)
    for val2 in nodes:

        point.next = Node(val2)
        print(point.next.value, end = '->')
        point= point.next


    #return(nodes)
    print('\n')
    return head.next.value


if __name__ == "__main__":

    list_1 = Node(1)
    list_1.next = Node(4)
    list_1.next.next = Node(5)

    list_2 = Node(1)
    list_2.next = Node(3)
    list_2.next.next = Node(4)

    list_3 = Node(2)
    list_3.next = Node(6)

    k_lists = [list_1, list_2, list_3]

    print((merge_lists(k_lists)))