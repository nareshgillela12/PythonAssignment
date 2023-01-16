# Q3. Write a generator function that yields the next prime number on each iteration.
#
# Sample Input output
#
# Input: 5
# Output: [2, 3, 5, 7, 11]
#
# Input: 10
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


from math import sqrt


def print_primenumbers(count):
    n = 1
    # k=10

    while count > 0:
        prime_flag = 0
        if (n > 1):
            for i in range(2, int(sqrt(n)) + 1):
                if (n % i == 0):
                    prime_flag = 1
                    break
            if (prime_flag == 0):
                # print(n)
                yield n
                count = count - 1
        n = n + 1


primecount = input("enter prime count")
# print(primecount)

result = ', '.join(str(prime) for prime in print_primenumbers(int(primecount)))
print(result)