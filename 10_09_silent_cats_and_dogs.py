#Challenge level - 2
from pathlib import Path

path = Path('cats.txt')
try: 
    contents = path.read_text('cats.txt')

except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
    pass


path = Path('dogs.txt')
try:
    contents = path.read_text('dogs.txt')

except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist")
    pass