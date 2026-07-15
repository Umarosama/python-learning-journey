#This program represents the basics Componants : 1)Input/Output 2)Operations 3)Variables 4)Expressions
#this is a simple elevator conversion program that takes the number of floors and converts it to the corresponding floor depending on the country.
#user enters the number of the floor -> enters where's he in US or Europe , the output shows the corrosponding floor cause in europe the ground floor is 0 not 1.




Floor = int(input("Enter the floor number: "))

Country = str(input("you are in the USA or Europe ? "))
if Country == 'USA' :
    print("The corrosponding floor in europe is : ")
    print(Floor-1)
else:
    print("The corrosponding floor in USA is : ")
    print(Floor+1)


