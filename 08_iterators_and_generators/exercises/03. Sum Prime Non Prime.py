simple_num = 0
counting_simple = 0
non_simple_num = 0

num = input()
while num != "stop":
    num = int(num)
    counting_simple = 0
    if num < 0:
        print('Number is negative.')
    else:
        for i in range(2, num):
            if num % i == 0:
                counting_simple += 1
        if counting_simple > 0:
            non_simple_num += num
        else:
            simple_num += num
    num = input()
print(f'Sum of all prime numbers is: {simple_num}')
print(f"Sum of all non prime numbers is: {non_simple_num}")



