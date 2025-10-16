#!/usr/bin/env python3
# Sample script that writes to a file
# By Sylent

import os
# dir_path = os.path.dirname(os.path.reathpath(__file__)) saves in current chapter

dir_path = os.path.dirname(os.path.realpath(__file__))

#open file for writing
test_file = open(dir_path + "/testfile.txt", "w")

#Write to File
test_file.write("What is your name?\n")
test_file.write("What is your favorite color?\n")
test_file.write("What was your first pet's name?\n")
test_file.write("What is your mother's maiden name?\n")
test_file.write("What elementary school did you attend?\n")




#Close the File
test_file.close()
