# reverse linked list O(n)

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class singlylinked:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = node(data)

        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def stack_reverse(self):

        s = []
        t = []
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            s.append(cur.data)  # knowledge graph lookup and look up gmatching

        for i in range(len(s)):
            t.append(s.pop())

        return t

    def length(self):
        count = 0
        cur = self.head

        while cur.next != None:
            cur = cur.next
            count += 1
        return (count)

    def remove(self, index):
        if index >= self.length():
            return 'error'
        cur_idx = 0
        cur = self.head

        while cur.next != None:  # in array of [1,2,3,4] last node = 2 lastnode.next= 3 cur node =3 cur node.next = 4
            last_node = cur  # put cur node.next contents into the lastnode.next content
            print(cur.data)
            cur = cur.next
            if cur_idx == index:
                last_node.next = cur.next
                return
            cur_idx += 1

    def swap_nodes(self, key1, key2):

        if key2 == key1:
            return

        cur1 = self.head
        prev1 = None

        while cur1 and cur1.data != key1:
            prev1 = cur1
            cur1 = cur1.next

        cur2 = self.head
        prev2 = None

        while cur2 and cur2.data != key2:
            prev2 = cur2

            cur2 = cur2.next

        if not cur1 or not cur2:
            return

        if prev1:
            prev1.next = cur2

        else:
            self.head = cur2

        if prev2:
            prev2.next = cur1

        else:
            self.head = cur1

        cur1.next, cur2.next = cur2.next, cur1.next

        return

    def remove_vowels(self):

        vowels = 'aeiou'

        cur = self.head

        while cur.next != None:  # in array of [1,2,3,4] last node = 2 lastnode.next= 3 cur node =3 cur node.next = 4
            last_node = cur  # put cur node.next contents into the lastnode.next content
            cur = cur.next
            # print(cur.next.data)
            if cur.data in vowels:  # access content of nodes with cur.data
                last_node.next = cur.next  # on next it. cur will still be there but will be deleted when you return list

        return

    def get_index(self, index):
        if index >= self.length():
            return 'error'
        cur_index = 0
        cur = self.head

        while True:

            cur = cur.next
            if cur_index == index:
                return (cur.data)
            else:
                cur_index += 1

    def print_list(self):

        nodes = []

        cur = self.head

        while cur:
            print(cur.data)
            # nodes.append((cur.data))
            cur = cur.next

        # print(nodes)

    def reverse_in_place(self):
        if self.length == 0:
            return
        prev = None
        cur = self.head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        self.head = prev
        return self

    def reverseUtil(self, curr, prev):

        # If last node mark it head
        if curr.next is None:
            self.head = curr

            # Update next to prev node
            curr.next = prev
            return

            # Save curr.next node for recursive call
        next = curr.next

        # And update next
        curr.next = prev

        self.reverseUtil(next, curr)
        print(curr.data)

    def reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)
        print(self.head.data)

    def merge(self, link2):

        s = None
        cur1 = self.head
        cur2 = link2.head

        if not self:
            return link2

        if not link2:
            return link1

        if cur1 and cur2:

            cur1 = cur1.next

            cur2 = cur2.next

            if cur1.data <= cur2.data:

                s = cur1
                cur1 = s.next

            else:
                s = cur2
                cur2 = s.next

            new_head = s

        while cur1 and cur2:

            if cur1.data <= cur2.data:

                s.next = cur1
                s = cur1
                cur1 = s.next

            else:

                s.next = cur2
                s = cur2
                cur2 = s.next

        if not cur1:
            s.next = cur2

        if not cur2:
            s.next = cur1

        self.print_list()
        return new_head.data

    def nth_to_last(self, n):

        """reverse the list then loop through"""

        # O(n)

        if n > self.length():
            return "Nth node doesn't exist"

        if n < 0:
            return "That's a negative number no go"

        self.reverse_in_place()

        if n == 0:
            return self.head.data

        cur = self.head
        n_count = 1

        while cur.next is not None:

            if n_count == n:
                # self.print_list()
                return cur.data

            cur = cur.next
            n_count += 1

    def tail_to_head(self):
        # count = 0

        cur = self.head
        # self.head= cur.next
        prev = None

        while cur.next != None:
            prev = cur
            cur = cur.next

        cur.next = self.head
        # self.head = cur
        prev.next = None
        # prev.next = None
        self.head = cur

        # return self.head.data

    def remove_duplicates(self):  # note to self can't store node address as dict key only the node values

        cur = self.head
        prev = None

        dups = dict()

        while cur:

            if cur.data in dups:
                prev.next = cur.next
                # cur = None
            else:
                dups[cur.data] = 1

                prev = cur
            cur = cur.next

    def rotate(self, k):
        p = self.head
        q = self.head
        prev = None

        count = 0

        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev
        while q:
            prev = q
            q = q.next
        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None

    def sum_two_lists(self, list1):

        p = self.head
        q = list1.head

        carry = 0

        summed_list = singlylinked()
        while p or q:

            if not p:

                p_data = 0

            else:
                p_data = p.data
                # print(p_data)

            if not q:

                q_data = 0

            else:
                q_data = q.data

            s = carry + p_data + q_data

            if s >= 10:

                carry = 1
                remainder = s % 10
                summed_list.append(remainder)
                # summed_list.print_list()

            else:
                carry = 0
                summed_list.append(s)

            if p:
                p = p.next

            if q:
                q = q.next

            if not q and not p:
                if carry == 1:
                    summed_list.append(carry)

        return summed_list

    def has_cycle(self):

        cur = self.head
        cur2= self.head

        while cur:
            print(cur.data)
            cur = cur.next

            if cur2.next.next is None:
                return False
            cur2= cur2.next.next


            if cur.data == cur2.data:
                return True






if __name__ == '__main__':
    sr = singlylinked()
    sr.append(1)
    sr.append(3)
    sr.append(9)
    sr.append(11)
    sr.append(11)
    sr.append(11)
    #sr.print_list()
    print(sr.has_cycle())
    #sr2 = singlylinked()

    #sr2.append(9)
    #sr2.append(7)
    #sr2.append(8)
    #sr2.print_list()



