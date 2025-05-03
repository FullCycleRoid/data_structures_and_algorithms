from typing import Any


class CustomList:
    def __init__(self):
        self.size = 0
        self._data = []


    def append(self, value: Any):
        self._data[self.size] = value
        self.size += 1