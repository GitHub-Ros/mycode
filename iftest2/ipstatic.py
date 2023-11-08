#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
    Conditional - strings test true"""

ipchk = "192.168.0.1"

# a string tests as true
if ipchk:
    print("Looks like the IP address was set: " + ipchk) #indented under if
else:    # if data is NOT provided
    print("You did not provide input.") # indented under else