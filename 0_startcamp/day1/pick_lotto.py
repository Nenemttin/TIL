import random

numbers = list(range(1, 46))

pick_numbers = random.sample(numbers, 6)
pick_numbers.sort()

print(pick_numbers)