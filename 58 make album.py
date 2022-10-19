def make_album (name_team, album_title, tracks=None):
    album_dic = {
    'artist':name_team.title(),
    'team': album_title.title()
    }
    if 'tracks':
        album_dic['tracks'] = tracks
    return album_dic

album = make_album ('jon','beland', tracks = 44)
print (album)
album = make_album ('al','bride')
print(album)
album = make_album ('hon','sun')
print (album)
