class Fibonacci:
    def __init__(self, n):
        self.total = n
        self.list = []
        self.prev = 0
        self.next = 1
    def __getitem__(self, p):
        return self.list[p]
    def __iter__(self):
        return self
    def __next__(self):
        if self.total == 0:
            raise StopIteration
        prev_ = self.prev
        next_ = self.next
        self.list.append(next_)
        self.prev, self.next = self.next, self.prev + self.next
        self.total -= 1
        return next_
