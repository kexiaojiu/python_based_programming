#!/usr/bin/env python3

def count_word_in_filename(filename, word):
	"""count how many 'word' in filename"""
	try:
		with open(filename) as fo:
			contents = fo.read()
	except FileNotFoundError:
		error_message = "Sorry, the file" + filename + " does not exits.\n"
		print(error_message)
		pass
		#~ with open('missing_files.txt', 'a') as missing_obj:
			#missing_obj.write(filename + "\n")
	else:
		num_word_in_filename = contents.lower().count(word)
		print("The file " + filename + " has about " + 
			str(num_word_in_filename) + " words '"+ word + "'.\n")
			
			
filenames = ['alicea.txt', 'the_sign_of_four.txt', 'a_study_in_scarlet.txt', 'the.txt']
word = 'the'
for filename in filenames:
	count_word_in_filename(filename, word)
