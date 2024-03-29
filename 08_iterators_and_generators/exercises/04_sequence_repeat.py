class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.pointer = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer < self.number:
            symbol = self.sequence[self.pointer % len(self.sequence)]
            self.pointer += 1
            return symbol
        raise StopIteration()


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

print("\n")
print("============================")

result = sequence_repeat('I Love Python', 2)
for item in result:
    print(item, end ='')
