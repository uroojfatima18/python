#ex 09      feet to inches

# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

# solution:
inches_in_foot:  int = 12

def main():
     feet=float(input("Enter a number of feet: "))   #get user input
     inches = feet * inches_in_foot      # to convert apply formula

     print(f"{feet} is equal to {inches}")   # print answer


 # This provided line is required at the end of
 # Python file to call the main() function.
if __name__ == '__main__':
     main()
