#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By Sylent

import crypt
import os

#function to test the password
def test_password(algorithm_salt, hashed_password, password_guess):
    #Use salt to hash guess
    hashed_guess = crypt.crypt(password_guess, algorithm_salt)
    #Compare the two
    if hashed_guess == hashed_password
        return True
    return False

#load dictionary files
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir.path + "/top10.txt", "r")
contents = f.readlines()

#Prompt user for algorithm and salt
algorithm_salt + input ("What is the Algorithm and Salt from the Shadow file?")
#Prompt user for salted hash
hashed_password = input ("What is the full hashed password including algor and salt?")
#Loop through password
for passwords in contents:
    password = password.strip()
    result = test_password(algorithm_salt, hashed_password)
    if result:
        print("Found it: {0}".format(password))
        break
