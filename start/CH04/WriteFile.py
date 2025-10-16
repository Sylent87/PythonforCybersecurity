#!/usr/bin/env python3
# Sample script that writes to a file
# By Sylent

import os
# dir_path = os.path.dirname(os.path.reathpath(__file__)) saves in current path

dir_path = os.path.dirname(os.path.realpath(__file__))

#open file for writing
hack_file = open("PID.txt", "w")

#Information to collect
print("Please answer the Following.")

user_name =input("What is your name? ")
fav_color =input("What is your favorite color? ")
pet_name =input("What was your first pet's name? ")
maiden_name =input("What is your mother's maiden name? ")
school_name =input("What elemetary school did you attend? ")

#Write to file.
hack_file.write("What is your name? " + user_name + "\n")
hack_file.write("What is your favorite color? " + fav_color + "\n")
hack_file.write("What was your first pet's name? " + pet_name + "\n")
hack_file.write("What is your mother's maiden name? " + maiden_name + "\n")
hack_file.write("What elementary school did you attend? " + school_name)

#Close the File
hack_file.close()