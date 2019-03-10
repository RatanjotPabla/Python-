#Name:              Ratanjot Pabla
#StudentNo:         32700826
#Date_Submitted:    October 26, 2018
#File_Name:         forSumSquares.py
#Teacher_Name:      Mr. Sarros
#Purpose:           This program will output the result for the sum of all the numbers from 1 to 100 within a 'for' loop. Each output should begin on a newline.  
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

total = 0   #The variable called total is assigned the value of 0.
for count in range(1,101):  #The 'for' loop. The condition being for count in range of (1,101) which will take the following line and do it from 1 to 100.
    total = (total+ count**2)   #The variable total is then equal to count squared plus the previous total. Adding the total with the count squared is what makes it 
                                #the program to calculate the sum.
    print(total)                #This prints all sums from 1 to 100, with each count being on a new line.
