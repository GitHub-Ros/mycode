#!/user/bin/env python3
"""Alta3 Research | RZFreeser
   print() - display data to std out"""

# below is a function containing our code
def main():

    # pause the programd and wait for the user to provide input
    user_input = input("Please enter an IPv4 IPaddress:")

    # display the input back to the user.
    print("You told me the IPv4 address is: " + user_input)

# this calls main
main()