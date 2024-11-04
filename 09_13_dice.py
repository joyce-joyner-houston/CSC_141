#Challenge level - 3
import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides


    def roll_dice(self):
        return random.randint(1, self.sides)
    

six_sided_die = Dice()
print("Rolling a 6-sided die 10 times:")
for _ in range(10):
    print(six_sided_die.roll_dice())


ten_sided_die = Dice(10)
print("\nRolling a 10-sided die 10 times:")
for _ in range(10):
    print(ten_sided_die.roll_dice())


twenty_sided_die = Dice(20)
print("\nRolling a 20-sided die 10 times:")
for _ in range(10):
    print(twenty_sided_die.roll_dice())
