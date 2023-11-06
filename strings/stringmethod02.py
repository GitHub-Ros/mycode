#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

def main():
    """ Run-time code"""
    
    # Create a small string
    lilstring = "Alta Research offers classes on Python coding"
    newlist = lilstring.split(" ") # this returns a list
    print(newlist)

    # Create a list of strings
    myiplist =["192", "168", "0", "12"]
    # Set singleip as the result of joining the list myiplist around the "."
    singleip = ".".join(myiplist)
    # Display singleip
    print(singleip)

# Call our main function
main()
