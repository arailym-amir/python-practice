# Exercise 4: Print all divisors of n
# d is a divisor of n when n % d == 0 (no remainder).
# Primes like 13 or 97 have exactly two divisors: 1 and themselves.

n = 36

for d in range(1, n + 1):
    if n % d == 0:
        print(d)
