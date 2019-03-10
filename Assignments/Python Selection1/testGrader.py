#Name:          Ratanjot Pabla
#StudentNo:     32700826
#Date:          October 02, 2018
#File_Name:     testGrader.py
#Teacher:       Mr. Sarros
#Purpose:       The program will ask the user to input their average on their
                #test. Then it will display a letter based on the percentile
                #the user inputs.

Student_Mark= int(input("What is your average on the test")) #This will ask the user to input their averge on their test(percentile).

if Student_Mark>= 90: #If the program reads that the integer inputted by the user is 90 or above, it will print the true branch below (the letter A).
    print("A")

elif Student_Mark>= 70: #If the program reads that the integer inputted by the user is 70 or above, it will print the true branch below (the letter B).
    print("B")

elif Student_Mark>= 60: #If the program reads that the integer inputted by the user is 60 or above, it will print the true branch below (the letter C).
    print("C")

elif Student_Mark>= 50: #If the program reads that the integer inputted by the user is 50 or above, it will print the true branch below (the letter D).
    print("D")

else:                  #Otherwise, if the percentile does not equal to any of the conditions above, which is getting a mark of 50 or above, the program will output
    print("F")         #the false branch below (the letter F). 
