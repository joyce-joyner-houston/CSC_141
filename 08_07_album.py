def make_album(artist, title, number_of_songs=None):
    album_info = {'artist': artist, 'title': title}

    if number_of_songs:
        album_info['number_of_songs'] = number_of_songs

    return album_info

album_1 = make_album('The Weeknd', 'Angel')
album_2 = make_album('Kendrick Lamar', 'Not Like Us')
album_3 = make_album('The Neighbourhood', 'Scary Love')

print(album_1)
print(album_2)
print(album_3)