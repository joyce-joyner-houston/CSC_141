#Counting to Twenty
for value in range(1, 21):
    print(value)


#My Pizzas, Your Pizzas
my_pizzas = ['sausage', 'buffalo chicken', 'meat lovers']
friends_pizzas = my_pizzas.copy()

my_pizzas.append('margherita')
friends_pizzas.append('pepperoni')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print("-", pizza)


print("My friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print("-", pizza)


#Buffet
buffet_foods = [
    'pasta', 'salad', 'burger', 'chicken', 'sushi'
    ]

print("The restaurant offers the following foods:")
for food in buffet_foods:
    print("-", food)

try:
    buffet_foods[0] = 'rice'
except TypeError as e:
    print("Error:", e)


buffet_foods = [
    'chicken', 'pizza', 'tacos', 'mac n chesse'
    ]

print("\nThe revised menu includes:")
for food in buffet_foods:
    print("-", food)