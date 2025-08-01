#LEARNING STRINGS


str= "hello!my name is urooj"
# print(str)

str= "hello!.\ni am learning python" #for next line
print(str)

str= "hello!. \t i am learning python" #for tab
print(str)

#concatenation
str1="Hello"
str2= "World"
print(str1+str2) #to concatenate  strings

str1="hey"
print (len(str1))
str2= "urooj"
print(len(str2))   #to find the length of string

final_string= str1  + " " + str2 # empty strings called space 
print(final_string)
print(len(final_string)) # space also count in len

#Indexing
str='hello world'
ch= str [1] # indexing means which num you give print same
print(ch) # print e

#slicing
str = "helloworld"
print(str[0:5])  #[0:5] means hello
print(str[0:(len(str))]) # len of str means last 

#Negetive index
str="HelloWorld"
print(str[-5:-1])  #backword counting

#STRINGS FUNCTIONS

str=("Hello i'm urooj")
print(str.endswith("ooj"))  #returns true if str ends with substr

str="urooj fatima"
print(str.capitalize()) #capatlized first charcter

str="i am studying python"
print(str.replace('python','javascript'))  #replace old value to new one

str="i am studying python"
print(str.find('t')) #find indexing

str='i am study python'
print(str.count('t'))

#PRACTICE 
#Q1
name=input('enter your name:')
print('length of your name is ', len(name)) # find a len
#Q2
str='its $ symbol and $89.99'
print(str.count('$'))  #find occurance of dollar