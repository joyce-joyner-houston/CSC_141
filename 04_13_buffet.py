buffet_foods = ['pasta', 'salad', 'burger', 'chicken', 'sushi']

print("The restaurant offers the following foods:")
for food in buffet_foods:
    print("-", food)

try:
    buffet_foods[0] = 'rice'
except TypeError as e:
    print("Error:", e)


buffet_foods = ['chicken', 'pizza', 'tacos', 'mac n chesse']

print("\nThe revised menu includes:")
for food in buffet_foods:
    print("-", food)