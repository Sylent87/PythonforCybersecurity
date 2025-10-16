#!/usr/bin/env python3
# Sample script that reads from a file
# By Sylent

hack_file = open("PID.txt", "r")
print("Here is someone to hack. - Information.")

contents = hack_file.read()
print(contents)

