#!/usr/bin/env python3
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program.\n"

message = ""
while message != 'quit':
		message = input(prompt)
		if message != 'quit':
			print(message)
