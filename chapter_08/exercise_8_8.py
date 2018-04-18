#!/usr/bin/env python3

def make_album(singer_name, album_name, number=''):
	if number:
		album = {'singer_name':singer_name, 'album_name':album_name,'number':number,}
	else:
		album = {'singer_name':singer_name, 'album_name':album_name}
	return album
	
while True:
	print("\nPlease tell me the names and number of songs :('q' to quit)")
	
	s_name = input("Please input the singer name: ")
	if s_name == 'q':
		break
	
	a_name = input("Please input the album name: ")
	if a_name == 'q':
		break
	
	number = input("Please input the number of songs: ")
	if number == 'q':
		break
		
	album = make_album(s_name, a_name, number)
	print(album)

