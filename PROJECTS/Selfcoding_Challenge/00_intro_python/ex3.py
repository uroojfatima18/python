#ex.3 :

# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

#solution:
def main():
    print("Convert Fahrenheit Temperature to Celsius! ")
    Temperature=(input("Enter  Temperatue in  Fahrenheit: "))  # input temperature
    temp=float(Temperature)                 # convert into float
    degree_celsius=((temp)- 32) * ( 5.0 / 9.0 )   # formula to convert fahrenheit into celsius
    print(f'Temperature: {temp}F ={degree_celsius}C')

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()