# Exercise 5: Collect divisors in a list and count them
# If the count is exactly 2, the number is prime.

n = 97
divisors = []

for d in range(1, n + 1):
    if n % d == 0:
        divisors.append(d)

print(divisors)
print(len(divisors))
