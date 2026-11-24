# Exercise 6: Sum 1 to 100 with a while loop
# A while loop repeats as long as the condition is True.
# i must increase each time (i += 1), otherwise the loop never ends.
# Note: avoid naming a variable "sum", because it overwrites the built-in sum().

i = 0
total = 0

while i <= 100:
    total += i
    i += 1

print(total)   # 5050

# Same result with the built-ins:
print(sum(range(1, 101)))
