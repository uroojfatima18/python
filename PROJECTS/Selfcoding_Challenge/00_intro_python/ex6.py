# ex 6 :
# Ask the user for a number and print its square (the product of the number times itself).

#solution:
def main():
    print(" This program is for square! ")
    number=(input('Enter a number:'))
    num =float(number)    # covert into floating value
    square = num * num 
    print(f'The square of {num} is {square}')


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()