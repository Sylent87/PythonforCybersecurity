#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By Sylent

import os

#prompt for file, and open
log_file = input("Which file do you want to see?")
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path + "/" + log_file, "r")

#read file by line
while True:
    line = f.readline()
    if not line:
        break
    #Look for 404, and print out 404
    if "404" in line:
        print(line.strip)

#close file
f.close()

