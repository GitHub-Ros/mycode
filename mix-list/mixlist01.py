#!/usr/bin/env python3

# Create a list containing three items

#my_list = [ "192.168.0.5", 5060, "UP" ]
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# Display the first item in the list

#print("The first item in the list (IP): " + my_list[0] )
print("The IP addresses on the list are: " + iplist[3] + " and " + iplist[4])

# Display the second item in the list

#print("The second item in the list (port): " + str(my_list[1]) )
print("The ports on the list are: " + str(iplist[0]) + " , " + iplist[1] + ", and " + str(iplist[2]))

# Display the third item in the list

#print("The last item in the list (state): " + my_list[2] )
print("The last item on the list is: " + iplist[5] )
