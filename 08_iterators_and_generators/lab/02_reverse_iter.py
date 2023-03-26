from typing import List


class reverse_iter:
    def __init__(self, list_to_reverse: List):
        self.list = list_to_reverse
        self.i = len(list_to_reverse) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 0:
            current = self.list[self.i]
            self.i -= 1
            return current
        raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
