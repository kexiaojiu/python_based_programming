#!/usr/bin/env python3

def make_album(singer_name, album_name, number=''):
	if number:
		album = {'singer_name':singer_name, 'album_name':album_name,'number':number,}
	else:
		album = {'singer_name':singer_name, 'album_name':album_name}
	return album
	
album1 = make_album('zhangjie', 'kk')
album2 = make_album('zhoujielun','zz', 5)
album3 = make_album('lil','zz', 6)

print(album1)
print(album2)
print(album3)

