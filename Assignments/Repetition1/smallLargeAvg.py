#Name:              Ratanjot Pabla
#StudentNo:         32700826
#Date_Submitted:    October 25, 2018
#File_Name:         smallLargeAvg.py
#Teacher_Name:      Mr. Sarros
#Purpose:           This program is used to figure out the smallest, largest and the average number in the collection of numbers the user inputs. First, the user is
                    #prompted to input the amount of numbers that they will like to input into the program. Then the user will be able to input "x" amount of numbers
                    #and have any value to it between 0-1000000000. Then once the user has finished inputting their collection of numbers, it will output the smallest
                    #number, largest number and the average throughout all the numbers in the collection. 

N_Value = int(input("How many numbers would you like to have?"))    #Prompts the user to input the 'x' amount of numbers they want in their collection.
counter,total = 0,0    #The variables called 'counter' and 'total' are both assigned the value of 0.   
smallest,largest = 1000000000,0     #The variables called 'smallest' is assigned the value of 1000000000 and the variable 'largest' is assigned the value of 0. 

while counter<N_Value:  #While the counter is less than the amount of numbers in the collection
    
    counter+=1  #The counter counts how many numbers the user has inputted, by increasing the counter by 1 each time a number is inputted into the program.
    value = float(input("Enter a number:"))    #Prompts the user to input the value of their number which will be a part of their collection of numbers.
    total+= value  #The total counter will continuously add the value of the number being inputted from value1 into their collection.
    
    if value<smallest:  #If the value is smaller than 1000000000, then it will replace the number in "value" and assign it into the variable "smallest." 
        smallest = value
        
    if value>largest:   #If the value is larger than 0, then it will replace the number in "value" and assign it into the variable "largest." 
        largest = value
        
    average = (total/N_Value)   #This will find the average by adding the value of all the numbers in the collection and dividing it by the number in "N_Value."

print("""The smallest number in your collection of numbers is %.2f. The largest number in your collection of numbers is
%.2f. The average of your list of numbers is %.3f"""%(smallest, largest, average))
#Finally, the program will output the smallest, largest, and the average from the collection of numbers inputted by the user.
 
    
