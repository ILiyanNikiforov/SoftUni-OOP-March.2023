def squares(num):
    i = 1
    while i <= num:
        yield i ** 2
        i += 1

    # With iterator:
# class squares:
#     def __init__(self, n):
#         self.n = n
#         self.start_num = 1

    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     while self.start_num <= self.n:
    #         current_num = self.start_num
    #         self.start_num += 1
    #         return current_num * current_num
    #     raise StopIteration()



print("\n".join(str(x) for x in list(squares(500000))))