# Max Heap

class Max_heap:
    def __init__(self,items=[]):


        # super().__init__()
        self.heap = []

        for i in items:
            self.heap.append(i)

            self._floatUp(len(self.heap) - 1)

    def __repr__(self):
        return ' '.join([str(i) for i in self.heap])

    def push(self, value):

        self.heap.append(value)

        self._floatUp(len(self.heap) - 1)

    def peek(self):

        if self.heap is not None:
            return self.heap[1]

    def pop(self):

        if self.heap is None:
            max = False

        if len(self.heap) > 2:
            self._swap(1, len(self.heap) - 1)

            max = self.heap.pop()

            self._bubble_down(1)

        if len(self.heap) == 2:
            max = self.heap.pop()

        return max

    def _swap(self, i, j):

        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _floatUp(self, index):

        parent = index // 2

        if index == 1:
            return

        elif self.heap[index] > self.heap[parent]:

            self._swap(index, parent)

            self._floatUp(parent)

    def _bubble_down(self, index):

        left = index * 2
        right = index * 2 + 1

        largest = index

        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left

        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right

        if largest != index:
            self._swap(index, largest)

            self._bubble_down(largest)


if __name__ == '__main__':
    g = Max_heap([35, 3, 21, 4])
    g.push(10)
    print(g)

