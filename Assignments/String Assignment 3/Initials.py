#Name:          Ratanjot Pabla
#StudentNo:     32700826
#File_Name:     Initials.py
#Teacher:       Mr.Sarros
#Purpose:       This program will ask the user for their full name. Then it will output their initials by combining the first letter from
                #their first and last name with a comma in the middle.



user_Name = input("What is your name(first & last)?")       #Asks the user for their full name.
first_Name = (user_Name[0])                                 #The variable first_Name is equal to the first letter of the name.
last_Name = (user_Name.split(" ")[1][0])                    #The variable last_Name is equal to the first letter of the last name.
print(first_Name+","+last_Name)                             #This will concatenate first_Name and last_Name to output the user's initials. 
