#  Data Structures
# {  List, tuple  , dictionary }

# List []
# 1.  Personal Book List
my_books=[]  # make list 
my_books.append("Namal")     #add name
my_books.append("Mala")         #
my_books.append("Amarbail")     #
print(my_books) 

my_books.remove("Namal")     # remove name
print(my_books)

print(len(my_books))         # length check
print(my_books)

# 2.  Book Management System

books = ['namal', 'peer-e-kamil', 'Mushaf', 'mala', 'amarbail']
print(books)  
user_input = input("Enter a book name: ")  # User se book ka naam lein
books.append(user_input)  # User ki book ko list mein add karein
print(books) 

books.remove('mala')  # 'mala' book ko list se remove karein
print(books)  

print(len(books))  # List ki length print karein
print(books)  # Final list print karein

# 3.Tuple ()
name=(1,)    # tuple, (1)not tuple

fav_color=("black","white","green")     # tuple
# print(len(fav_color))
print(fav_color)
fav_color[1]     #indexing

fav_color[0:2]      #slicing

fav_color=fav_color.count('black')        # count
print(fav_color)

fav_color2=("mustard","blue")          #concatenate
fav_color3=fav_color+fav_color2
print(fav_color3)

fav_color=fav_color3*2       # repeat
print(fav_color)

fav_color=("black","white","green",),("mustard","blue" )    # nested tuple
print(fav_color)