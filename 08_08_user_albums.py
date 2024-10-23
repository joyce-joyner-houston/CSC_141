def make_album(artist, title, number_of_songs=None):
    album_info = {'artist': artist, 'title': title}

    if number_of_songs:
        album_info['number_of_songs'] = number_of_songs

    return album_info


while True:
    print("\nEnter album details:")
    artist = input("Artist name (or 'quit' to exit):")
    if artist.lower() == 'quit':
        break

    title = input("Album title: ")
    number_of_songs_input = input("Number of songs (press enter to skip): ")
    number_of_songs = int(number_of_songs_input) if number_of_songs_input else None

    album = make_album(artist, title, number_of_songs)
    print(album)
