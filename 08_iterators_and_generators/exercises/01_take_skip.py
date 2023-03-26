class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.i = 0
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.count:
            current = self.num
            self.num += self.step
            self.i += 1
            return current
        raise StopIteration()


numbers = take_skip(2, 6)
for number in numbers:
    print(number)


print("--------------------------")


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
