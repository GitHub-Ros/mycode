#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # Create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # Display list1
    print(list1)

    # Display list[1]
    print(list1[1])

    # Create a new list containing a single item
    list2 = ["juniper"]

    # Extend list1 by list2 (combine both lists together into a single list)
    list1.extend(list2)

    # Display list1, which now contains juniper
    print(list1)

    # Create list3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    # Use the append operation to append list1 by list3
    list1.append(list3)

    # Display the new complex list1
    print(list1)
    
    # Display the list of IP addresses
    print(list1[4])
    
    # Display the first item in the list (0th item) - first IP address
    print(list1[4][0])

main()
