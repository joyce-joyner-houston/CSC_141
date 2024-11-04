#Challenge level - 2
import random

lottery_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

winning_elements = random.sample(lottery_elements, 4)

print(f"Winning elements: {winning_elements}")
print("Any ticket matching these 4 numbers or letters wins a prize!")
