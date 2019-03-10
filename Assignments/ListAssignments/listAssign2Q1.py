#Name:              Ratanjot Pabla
#StudentNo:         32700826
#Date_Submitted:    November 19, 2018
#File_Name:         listAssign2Q1.py
#Teacher_Name:      Mr. Sarros
#Purpose:           This program will prompt the user for their marks in the class which will be stored inside a list. For the student or teacher to end the list of
                    #marks in the list, they must type in -1 when they are asked, "What is your mark?." Later, the program will output the smallest, largest, average
                    #and the median mark in the list. To do so, all the marks will be sorted out in a list, making the first element the smallest mark
                    #and the last element the largest mark. To find the average, the program will simply just find the sum of the marks and divide it by the length
                    #of the total number of elements. Finally, to find the median, the program will output the middle number of the list. If their is an even number
                    #of marks inputted, then it will take the sum of the two middle numbers and divide it by two. 

x = []  #empty list 


while True:
    number = int(input("What is your mark?"))   #This will prompt the user to input their marks and will continue to do so until the user inputs -1 to end the prompt. 

    if number == -1:    #If the user inputs -1, then it will break the user prompt. The marks will be all the numbers inputted before -1.
        break

    x.append(number)    #This is what adds(append) all the marks(number) into the list. 
x.sort()    #This is what sorts the list from the smallest to the largest number in the list. 
print ("The lowest mark in your list is",x[0])    #This will print the first element in the list which is also the lowest mark.
print("The highest mark in your list is",x[-1])     #This will print the last element in the list which is also the largest mark. 

Length = (len(x))   #The variable 'Length' is assigned to the length of the number of elements in the list.
ave = sum(x)/Length     #The variable 'ave' is assigned to the sum of elements in the list divided by the length of the amount of numbers inputted. 
print("The class average is %.2f"%(ave))   #Print statement for the average. 

if Length % 2 == 0: #If the length of the total number of elements is divisible by 2 without having a remainder, then there are an even amount of numbers in the list.
    Length = int(Length/2)  #This will take the second mark of the two middle numbers in the list.
    value = int(Length-1)   #This will take the first mark of the two middle numbers in the list.
    print ("The median of the class is",(x[value] + x[Length])/2) #A final print statement which will add the two middle numbers and divide it by two, printing the
                                                                #number in between the two middle numbers. For an example, the middle number in between 2 and 3 is 2.5.
    
else:   #If the length of the total number of elements is not divisible by and will have a remainder of 1, then there are an odd amount of numbers in the list. 
    Length = str(Length/2)  #This will take the total amount of elements and divide it by 2. Leaving the variable 'Length' to equal a decimal(whole number with .5)
    value = int(Length[0])  #This will take the index of the first character in the decimal number stored in the variable 'Length' 
    print("The median of the class is",x[value])  #This will output the median of the class by outputting the mark of the index of value in the list 'x'.
    



    
    


