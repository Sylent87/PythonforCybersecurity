#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By Sylent on OCT 23

# Prompt for the source message
message = input("What is the message to encrypt/decrypt? ")
# Convert message to lower-case for simplicity
message = message.lower()
final_message = ""

# Loop through each letter in the source message
for letter in message:
    # Convert the letter to the ASCII equivalent
    ascii_num = ord(letter)
    # Check to see if an alphabetic (a-z) character, 
    # if not, skip
    if ascii_num >= 97 and ascii_num <= 122:
        # Add 13 to ascii_num to "shift" it by 13
        new_ascii = ascii_num + 13
        # Confirm new character will be alphabetic 
        if new_ascii > 122:
            # If not, wrap around
            new_ascii = new_ascii - 26
        final_message = final_message + chr(new_ascii)
    else:
        final_message = final_message + chr(ascii_num)

# Print converted message
print("Message has been converted:")
print(final_message)