#ex 02



#solution:
speed= 299792458        #value of speed(constant)
def main():
    mass=float(input("Enter kilos in mass : "))  #user mass input
    energy = mass* speed **2      #apply formula to calculate energy
 
    print(f"{energy} joules of energy! ")   #print 


main()    