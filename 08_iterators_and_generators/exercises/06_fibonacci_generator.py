def fibonacci():
    num1 = 0
    num_2 = 1

    yield num1
    yield num_2

    while True:
        next_num = num1 + num_2
        yield next_num
        num1 = num_2
        num_2 = next_num


generator = fibonacci()
for i in range(5):
    print(next(generator))

print("--------------")

generator = fibonacci()
for i in range(1):
    print(next(generator))
