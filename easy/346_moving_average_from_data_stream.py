class MovingAverage:
    """
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
    """
    # Second method getting MA without creating a new data structure
    def __init__(self, size: int):
        self.index = 0
        self.ma_size = size
        self.ma_list = []

    def next(self, val: int) -> float:
        self.ma_list.append(val)
        self.index = len(self.ma_list)-1
        if len(self.ma_list) > self.ma_size:
            # The last concat needs to be index + 1
            # eg. ma_list = [1, 10, 3, 5] --> ma_list[1:4] --> [10, 3, 5]
            return sum(self.ma_list[self.index-self.ma_size+1:self.index+1]) / self.ma_size
        else:
            return sum(self.ma_list) / len(self.ma_list)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
"""
Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
"""

