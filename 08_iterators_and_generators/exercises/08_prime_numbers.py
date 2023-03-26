from typing import List


def is_prime(num):
    count_simple = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                count_simple += 1
        if count_simple == 0:
            return True


def get_primes(my_list: List):
    for num in my_list:
        if is_prime(num):
            yield num



print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
