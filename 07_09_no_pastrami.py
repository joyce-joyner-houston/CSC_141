sandwich_orders = ['ham', 'pastrami', 'turkey', 'pastrami', 'tuna', 'pastrami', 'club']
finished_sandwiches = []

print("The deli has run out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)


print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")