# Exercise 2: Lists, indexing, slicing, sum and sorting

nums = [3, 8, 15, 22, 7]

print(nums[0])          # first item
print(nums[-1])         # last item (negative index counts from the end)
print(len(nums))        # number of items

# sum with a loop (practice) and with the built-in
total = 0
for num in nums:
    total += num
print(total)
print(sum(nums))

print(nums[:3])         # first three items (slice)
print(sorted(nums))     # sorted copy; the original list is unchanged
