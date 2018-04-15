#!/usr/bin/env python3

# Firstly, build a list for unconfirmed users and a list for confirmed users
unconfirmed_users = ['alice0', 'brian', 'candace']
confirmed_usres = []

# Secondly, confirm every user in the list until there is no unconfirmed user
# then move confirmed users to the list of confirmed users
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	
	print("verifying user: " + current_user.title())
	confirmed_usres.append(current_user)

# At last, print all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_usres:
	print(confirmed_user.title())
	
