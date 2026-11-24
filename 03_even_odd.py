# Exercise 3: Even or odd from 1 to 20
# A number is even when dividing by 2 leaves remainder 0 (n % 2 == 0).

for number in range(1, 21):
    if number % 2 == 0:
        print(f"even: {number}")
    else:
        print(f"odd: {number}")
