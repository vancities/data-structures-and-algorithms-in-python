class Array(object):
    def __init__(self, size=32):  # 关键属性：分配空间和存储单位（使用列表的单个元素作为一个存储单位）
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):  # Called to implement evaluation of self[index]实现下标访问.
        return self._items[index]

    def __setitem__(self, index, value):  # Called to implement assignment to self[index].
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class MinHeap(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count - 1)

    def _siftup(self, ndx):
        if ndx > 0:
            parent = (ndx - 1) // 2
            if self._elements[ndx] < self._elements[parent]:
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
                self._siftup(parent)

    def extract(self):
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._siftdown(0)
        return value

    def _siftdown(self, ndx):
        left = (ndx * 2) + 1
        right = (ndx * 2) + 2
        # 找出当前节点及左右子节点中的最小值，与当前节点交换位置，并递归地对换下去的节点执行siftdown操作
        smallest = ndx
        if left < self._count and self._elements[left] < self._elements[smallest] and right < self._count and \
                self._elements[left] <= self._elements[right]:
            smallest = left
        elif left < self._count and self._elements[left] < self._elements[smallest] and right >= self._count:
            smallest = left
        elif right < self._count and self._elements[right] < self._elements[smallest]:
            smallest = right
        if smallest != ndx:
            self._elements[ndx], self._elements[smallest] = self._elements[smallest], self._elements[ndx]
            self._siftdown(smallest)


def test_maxheap():
    import random
    n = 10
    h = MinHeap(n)
    mylist = list(range(n))
    random.shuffle(mylist)
    for i in mylist:
        h.add(i)
    for i in range(n):
        assert i == h.extract()
