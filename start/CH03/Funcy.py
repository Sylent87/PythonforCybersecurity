#!/usr/bin/env python3
# example workign with Loops
#By Sylent on Oct 18

#User Orompt
user_answer = str(input("Is today a good day? (y/n) "))


def send_message( my_message ):
    print(my_message)
    if user_answer == "y":
        for x in range(10):
            print("Yes it is!")
