class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity of jar can't be negative")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size*"🍪"

    def deposit(self, n=0):
        if self._size + n > self._capacity:
            raise ValueError("You are exceeding the jar capacity")
        self._size += n

    def withdraw(self, n=0):
        if n > self._size:
            raise ValueError("There are less cookies in the jar then asked to remove")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
