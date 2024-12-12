#Arithemetic operators
a= 8
b= 2

print(a+b)  # for add
print(a-b)  #for subtract
print(a*b)  #for multiply
print(a/b)  #for divide
print(a%b)  # for modulus means remainging
print(a**b) # for Exponentiation means 2 times multiply
print (a//b) #floor division means removes decimal part

# relational operators
a =8
b=2
print(a==b) # equal to
print(a!=b) #not equal
print(a>b) #Greator than
print(a<b) #less than
print(a<=b) #less than or equal to
print(a>=b) #Greator than or eqaul to

# #assingment operators
num=10
num= num+10  #10+10=>20
print(num)

num = 10
num = num + 5
print("num: ", num) # num:5

#logical operators
a=60
b=10
print(not True) #bool value ka opposite
print(not (a>b))

val1 =True
val2 =False
print("AND operator:", val1 and val2) #ans True: when both are true
print("OR operator:", val1 or val2)  # ans True : if 1 value is True

a=28
b= 50
c= 35
print(28+35+50)

# type conversation

# num = ("enter your age:")
# print("My age is" ,num)  # my age is ..


name = input(str('enter your name: '))
age = int(input('enter your age: '))
marks= float(input('enter your marks:'))

print('hi =', name )
print ('age =',age)
print ('marks=',marks )

first= int(input ('enter first number:'))
second= int(input ('enter second number:'))
print('sum=', first +second)


a = float(input("Enter your fav number: "))
b = float(input("Enter your secong fav number: "))

print("average =", (a + b) / 2)