#!/usr/bin/env python3

def count_words(filename):
	"""count words in files"""
	try:
		with open(filename) as fo:
			contents = fo.read()
	except FileNotFoundError:
		#~ error_message = "Sorry, the file" + filename + " does not exits."
		pass
		#~ print(error_message)
		#~ with open('missing_files.txt', 'a') as missing_obj:
			#missing_obj.write(filename + "\n")
	else:
		# count how many words in the file
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + 
			" words")
			
#~ filename = 'alice.txt'
#~ count_words(filename)

filenames = ['alice.txt', 'sddhartrha.txt', 'guest_book.txt', 'missing_files.txt']
for filename in filenames:
	count_words(filename)
