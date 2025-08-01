# Write a function that takes a list of numbers and returns the sum of those numbers.

#solution:

def sum_of_numbers(numbers): #custom function
    return sum(numbers)

numbers:list[int]= [1,2,3,4,5]
result = sum_of_numbers(numbers)
print(result)
