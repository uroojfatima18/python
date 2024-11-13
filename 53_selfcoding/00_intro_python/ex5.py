# ex .5 :

# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).


#solution :
def main():
    print("This program for Triangle length and calculation! ")
    # get three side length of tringle by user 
    side_1=float(input('what is the length of side 1 ? '))
    side_2=float(input('what is the length of side 2 ? '))
    side_3=float(input('what is the length of side 3 ? '))

    perimeter= side_1 + side_2 + side_3        # sum of  three length  sides
    print(f'The perimeter of triangle is :{perimeter}')       # total perimeter of triangle

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()