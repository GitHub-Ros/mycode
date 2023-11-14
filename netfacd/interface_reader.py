#!/usr/bin/env python3
"""Alta3 Research | Exploring interaces library"""

import netifaces

def find_mac(interface_name):
    """passed interface name (string), returns the MAC of that interface (string)"""
    return (netifaces.ifaddresses(interface_name)[netifaces.AF_LINK])[0]['addr']

def find_ip(interface_name):
    """passed interface name (string), returns the IP of that interface (string)"""
    return (netifaces.ifaddresses(interface_name)[netifaces.AF_INET])[0]['addr']

def main():
    """runtime"""

    print(netifaces.interfaces())

    for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try: # This is a new line, you also need to indent the code below this line by 4 whitespaces
            print('MAC: ', find_mac(i)) # This print statment will always print MAC without an end of line


            print('IP: ', find_ip(i)) # This print statement will always print IP without an end of line
        except: # This is a new line
            print('Could not collect adapter information') # Print an error message

if __name__ == "__main__":
    main()
