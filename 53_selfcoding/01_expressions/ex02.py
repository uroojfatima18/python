#ex 02

# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2

# Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.


#solution:
speed= 299792458        #value of speed(constant)
def main():
    mass=float(input("Enter kilos in mass : "))  #user mass input
    energy = mass* speed **2      #apply formula to calculate energy
 
    print(f"{energy} joules of energy! ")   #print 

main()    