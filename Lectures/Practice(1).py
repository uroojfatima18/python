#   # if, else practice questions

#  # practice 1. 
# age= int(input('Enter you age:'))
# if age < 18:
#    print(' You are not allowed to drive.')
# else:
#   print('you are allowed to drive.')

# # practice 2.
# tempereture=float(input('Enter your tempereture:'))
# if tempereture < 98.6 :
#    print('you have a  fever.')
# else:
#   print("you don't have fever.")

# # practice 3.
# number=int(input('Enter any number:'))
# if number > 100:
#   print('yes')
# else:
#   print('No')  

# #practice 4.
# marks=int(input('Enter your marks:'))
# if marks< 40:
#   print('fail')
# else: 
#    print('pass')

# #practice 5.
# number=int(input('Enter number:'))
# if number % 5 == 0 :
#    print('yes')
# else:
#    print("No")  

# practice 1 of nested  if else.
# if else nested 

number=int(input("Enter your marks:"))
if 0 <= number <= 100:
  if number > 90:
    Grade="A"
  if number > 80  and number <90:
    Grade="B"
    if number > 70 and number < 80:
      Grade="C"
      if number > 60 and number <70:
        Grade = "D"
        if number > 50 and number < 60:
          Grade =" E" 
          if number >60 and number < 50 :
            Grade="F"

    print("Grade:",Grade)
else:
    print("Invalid Output.")
   