#Name:              Ratanjot Pabla
#StudentNo:         32700826
#Date_Submitted:    October 30, 2018
#File_Name:         armstrongNum.py
#Teacher_Name:      Mr. Sarros
#Purpose:           This program is used to output all the three-digit armstrong numbers. To do so, I must take all the numbers from 100 to 999. Then, the program
                    #will cube each place value in the numbers from 100 to 999 and add them together. If the sum of the cubes is equal to the number itself,
                    #it will be known as a three-digit armstrong number. For an example, 1^3 + 5^3 + 3^3 = 153 (Notice how the base number of the place values in 153
                    #are in the same order as the digits in 153).
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
for number in range (99,999):   #The range of all three digit numbers starting from 100 and ending at 999.
    number+=1   #A counter that adds one to the previous number, which makes the number increase by one each time from 100 to 999.
    number = ((str(number)))    #This makes each number to be assigned the three-digit number as a string. 

    first_Digit = (int(str(number[0]))) #The first digit in the number is assigned as an integer and string.
    second_Digit = (int(str(number[1])))    #The second digit in the number is assigned as an integer and string.
    third_Digit = (int(str(number[2]))) #The third digit in the number is assigned as an integer and string.
    sumCubed_Digits = ((first_Digit**3)+(second_Digit**3)+(third_Digit**3)) #The sum of the first, second and third digit, each being cubed is assigned to the
                                                                            #variable name sumCubed_Digits
    
    sumCubed_Digits =((str(sumCubed_Digits)))   #The variable sumCubed_Digits is assigned as a string; which will be used for the if statement later on. 
    
    
    if number == sumCubed_Digits:   #If the number is equal to the sumCubed_Digits(equal to each the sum of each digit in 'number' cubed), it will print the
                                    #true branch below.
        print("A 3-digit armstrong numbers is %s"%(number)) #Print statement of all the 3- digit armstrong numbers.
    

