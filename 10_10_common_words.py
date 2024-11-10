from pathlib import Path

def count_words(path):
    try: 
        contents = path.read_text(path)

    except FileNotFoundError:
        print(f"Sorry file could not be found")

    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

path = Path('sample_text.txt')
count_words(path)