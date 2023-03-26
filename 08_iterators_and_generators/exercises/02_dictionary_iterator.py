class dictionary_iter:

    def __init__(self, my_dict: dict):
        self.dict = my_dict
        self.size = len(my_dict)
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.size:
            current = self.i
            self.i += 1
            return list(self.dict.items())[current]
        raise StopIteration()



result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
print("-------------------")
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
