#Challenge level 6
from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
new_text = contents.replace('Python', 'C')
print(new_text)