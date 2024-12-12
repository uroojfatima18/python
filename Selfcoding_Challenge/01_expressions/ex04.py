#ex04 

# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry. It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.
# For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:

# BC ** 2 = AB ** 2 + AC ** 2

#solution:

# import math   
def main():
    ab=float(input("Enter a length AB: ")) 
    ac=float(input("Enter a length AC: "))
    bc:float=math.sqrt(ab**2 + ac**2)     # function math.sqrt for square root 
    print("The length of BC (the hypotenuse) is: " + str(bc))      

    bc_squared = ab**2 + ac**2
    print("The square of BC is: " + str(bc_squared)) 

main()    
