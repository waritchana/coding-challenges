class MovingAverage:
    def __init__(self, size: int):
        self.ma = [''] * size
        self.index = 0
        self.size = size

    def next(self, val: int) -> float:
        self.ma[self.index] = val
        self.index = (self.index + 1) % self.size
        count_empty = self.ma.count('')
        if count_empty > 0:
            return sum(self.ma[0:-count_empty]) / (self.size-count_empty)
        else:
            return sum(self.ma) / self.size


# Your MovingAverage object will be instantiated and called as such:
# ["MovingAverage","next","next","next","next"]
# [[3],[1],[10],[3],[5]]
# Expect [null,1.00000,5.50000,4.66667,6.00000]
obj = MovingAverage(3)
param_1 = obj.next(1)
param_2 = obj.next(10)
param_3 = obj.next(3)
param_4 = obj.next(5)
print(
    ['null', param_1, param_2, param_3, param_4]
)
