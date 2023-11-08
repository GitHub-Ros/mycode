
def main():
    print("Module #1 Name=", __name__)

if __name__ == "__main__":
    print("Code is being run directly from Python.")

else: 
    print("Code is being run indirectly from import.")
    main()
    
    print("This code will always execute.")

def main():
   print("This code belongs to the main function in module 1.")

if __name__ == "__main__":
   main()

