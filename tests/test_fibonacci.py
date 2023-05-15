import pytest
from fibonacci import *

class TestFibonacci:
    def setup(self):
        self.fib = Fibonacci(6) # [1, 1, 2, 3, 5, 8]

    def test_iter(self):
        ob = iter(self.fib)
        output = 0
        for elem in ob:
            output += elem
        assert output == 20

    def test_next(self):
        assert next(self.fib) == 1
        assert next(self.fib) == 1
        assert next(self.fib) == 2
        assert next(self.fib) == 3
        assert next(self.fib) == 5
        assert next(self.fib) == 8
        with pytest.raises(StopIteration):
            assert next(self.fib)
