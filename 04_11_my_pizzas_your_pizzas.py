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