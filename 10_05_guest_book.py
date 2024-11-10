#Challenge level - 5
from pathlib import Path

path = Path('guest_book.txt')

while True:
    name = input("What is your name? (Enter 'quit' to stop): ")


    if name.lower() == 'quit':
        print("Thanks for signing the guest book!")
        break

path.write_text(Path)