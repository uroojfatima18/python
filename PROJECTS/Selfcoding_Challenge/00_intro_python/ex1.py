#  ex.1:    _add_2_numbers   

# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:
# Prompt the user to enter the first number.
# Read the input and convert it to an integer.
# Prompt the user to enter the second number.
# Read the input and convert it to an integer.
# Calculate the sum of the two numbers.
# Print the total sum with an appropriate message.

#solution:
print("This program adds two numbers.")
num_1=(input("Enter first number:"))     # user input  for first num
first_num = int(num_1)                  # Convert input to integer
num_2=(input("Enter Second number:"))  # user input for second num
second_num = int(num_2)               # Convert input to integer
# Responding with the user's input
total_sum= first_num + second_num        # calculate sum of two num
print('The total sum is:' ,total_sum)      # Display the total sum
