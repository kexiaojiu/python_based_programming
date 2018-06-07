#!/usr/bin/env python3
import json

def get_stored_username():
    filename = 'username.json'

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
       return None
    else:
        return username
            
def get_new_name():
    filename = 'username.json'
    username = input("What is your name?")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
        
def check_username(username):
    print("Is " + username + " your name?(Y/N)")
    flag = input("Enter 'N/n' to enter your true name, Enter 'Y/y' to continue: ")
    if flag.lower() == 'n':
        true_username = get_new_name()
    else:
        true_username = username
    
    return true_username
    
        
def greet_user():
    username = get_stored_username()
    if username:
        username = check_username(username)
        print("Welcome back, " + username + "!")
    else:
        username = get_new_name()
        print("We'll remember you when you come back, " + username + "!")
        
greet_user()
