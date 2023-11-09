#!/usr/bin/env python3

def bottles_of_beer(num):
    
    if num == 0:
       return "No more bottles of beer on the wall, no more bottles of beer.\n" \
              "Go to the store and buy some more, 99 bottles of beer on the wall.\n"

    lyrics = f"{num} {'bottles' if num > 1 else 'bottle'} of beer on the wall, {num} {'bottles' if num > 1 else 'bottle'} of beer.\n" \
             f"Take one down, pass it around, {num - 1} {'bottles' if num - 1 != 1 else 'bottle'} of beer on the wall.\n"
    return lyrics
# Using a for loop to print the lyrics for each verse
for i in range(99, 0, -1):
    print(bottles_of_beer(i))
