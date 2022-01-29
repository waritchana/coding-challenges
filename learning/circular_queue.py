class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.queue = [''] * k
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.queue[self.tail] = value
            if self.tail == self.k-1:
                self.tail = 0
            else:
                self.tail += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue[self.head] = ''
            if self.head+1 == self.k:
                self.head = 0
            else:
                self.head += 1
            return True

    def Front(self) -> int:
        # self.head points to the index to be dequeued
        # do -1 to get the actual last index
        if not self.isEmpty():
            return self.queue[self.head-1]
        return -1

    def Rear(self) -> int:
        # self.head points to the index to be enqueued
        # do -1 to get the actual last index
        if not self.isEmpty():
            return self.queue[self.tail-1]
        return -1

    def isEmpty(self) -> bool:
        return self.queue.count('') == self.k

    def isFull(self) -> bool:
        return self.queue.count('') == 0


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
param_1 = obj.enQueue(1)
param_2 = obj.enQueue(2)
param_3 = obj.enQueue(3)
param_4 = obj.enQueue(4)
param_5 = obj.Rear()
param_6 = obj.isFull()
param_7 = obj.deQueue()
param_8 = obj.enQueue(4)
param_9 = obj.Rear()
print(
    ["null", param_1, param_2, param_3, param_4, param_5,
    param_6, param_7, param_8, param_9]
)

# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
