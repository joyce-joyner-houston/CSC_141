import random

lottery_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B','C', 'D', 'E']
my_ticket = random.sample(lottery_elements, 4)

draws = 0

while True:
    draws += 1
    winning_elements = random.sample(lottery_elements, 4)
    if set(my_ticket) == set(winning_elements):
        break

print(f"It took {draws} draws to win with the ticket {my_ticket}!")