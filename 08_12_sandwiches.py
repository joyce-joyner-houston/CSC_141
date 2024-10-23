def make_sandwich(*items):
    print("What would you like on your sandwich?")
    for item in items:
        print(f"- {item}")

make_sandwich('turkey', 'lettuce', 'tomato')
make_sandwich('ham', 'cheese')
make_sandwich('peanut butter', 'jelly')