# Write a program that doubles each element in a list of numbers. For example, if you start with this list:
# numbers = [1, 2, 3, 4]
# You should end with this list:
# numbers = [2, 4, 6, 8]

# solution:
def main():
    numbers = [1, 2, 3, 4]

    double_num =[]
    for num in numbers:
         double_num.append(num*2)
    print(double_num)    

main()