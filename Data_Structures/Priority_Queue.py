"""
    Priority Queue is an extension of the queue with following properties.
        1) An element with high priority is dequeued before an element with low priority.
        2) If two elements have the same priority, they are served according to their order in the queue.

"""
class p_queue:

    def __init__(self):

        self.prio_queue = []

    def __repr__(self):  #can use __repr__ or __str__ to represent a string

        return ' '.join([str(i) for i in self.prio_queue])


    def is_empty(self):

        return len(self.prio_queue) == 0


    def insert(self,value):

        self.prio_queue.append(value)


    def delete(self):

        try:
            max = 0

            for i in range(len(self.prio_queue)):
                if self.prio_queue[i] > self.prio_queue[max]:
                    max = i

            item = self.prio_queue[max]
            del self.prio_queue[max]
            return item
        except IndexError:
            print()
            exit()


if __name__ == '__main__':
    myQueue = p_queue()
    myQueue.insert('a')
    myQueue.insert('d')
    #myQueue.insert(14)
    #myQueue.insert(7)
    print(myQueue)
    while not myQueue.is_empty():
        print(myQueue.delete())