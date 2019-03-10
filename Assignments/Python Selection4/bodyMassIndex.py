#Name:              Ratanjot Pabla
#StudentNo:         32700826
#Date_Submitted:    October 15, 2018
#File_Name:         bodyMassIndex.py
#Teacher_Name:      Mr. Sarros
#Purpose:           This program is used to find out the body mass index of a human being and come up with a conclusion if they are either underweight,
                    #normal, overweight or obese. To do so, the program will prompt the user for their name, weight, height, as well as, which method they
                    #would like to use, either imperial or metric scale. These two scales each have a different formula, both resulting with the same BMI
                    #as the final output after the calculations. 

user_Name = input("Please enter your name:")    #This prompts the user to input their name.
system_Measurement = input("What system of measurement would you like to use, imperial or metric measurement. Type 'i' for imperial or 'm' for metric.")    
    #This will prompt the user to input if they would like to use the inperial method by typing letter 'i' or the metric method by typing letter 'm'.

while True: #This is a while true loop which will output whatever it sees underneath, after the input follows the true branch or false branch.
    if system_Measurement != "m" and system_Measurement!= "i":  #If the measurement inputted is not i or m, it will ask the user to input again.
        system_Measurement = input("That is an incorrect input. You must type in either 'm' or 'i'.")
    else:
        break   #Otherwise, the program will break.

if system_Measurement == "i":   #If the user chooses the letter 'i' for imperial, it will follow the code below.   
    print("You have selected the imperial measurement.")    #This prints out that you've selected the imperial method to solve for your BMI.
    imperial_Weight = float(input("What is your weight(lbs)?")) #This prompts the user to input their own weight(lbs).
    imperial_Height = float(input("What is your height(inches)?"))  #This prompts the user to input their own height(inches).
    imperial_BMI_numerator = (imperial_Weight*703)  #The formula is equal to the user's weight times 703 divided by the user's height squared. This is the
                                                    #numerator of the formula.
    
    
    imperial_BMI_denominator = (imperial_Height**2) #This is the denominator of the formula.
    imperial_BMI_calculator = (imperial_BMI_numerator/imperial_BMI_denominator) #The BMI calculator variable will take the numerator divided by the                                                                                 #denominator to get the final BMI.
    if imperial_BMI_calculator < 18.5:  #If the BMI is less than 18.5,  it will display that the user is underweight. 
        BMI_statement = ("underweight")

    if imperial_BMI_calculator >= 18.5 and imperial_BMI_calculator <= 25:   #If the BMI is between 18.5 and 25, it will display that the user is normal.
        BMI_statement = ("normal")

    if imperial_BMI_calculator > 25 and imperial_BMI_calculator < 30:   #If the BMI is over 25 but less than 30, the user is overweight. 
        BMI_statement = ("overweight")

    if imperial_BMI_calculator >=30:    #If the BMI is 30 and over, the user is obese.
        BMI_statement = ("obese")
        
    print("""%s, with a height of %i inches and a weight of %i pounds, you have a BMI of %.2f. This is considered %s."""%     
(user_Name, imperial_Height, imperial_Weight, imperial_BMI_calculator, BMI_statement))
    #This will give the final statement, by outputting the user's name, their weight in lbs, their height in inches, their final BMI and a final statement
    #of their index (underweight,normal, overwieght or obese).

    
if system_Measurement == "m":   #If the user chooses the letter 'm' for metric, it will follow the code below.
    print("You have selected the metric measurement.")  #This prints out that you've selected the metric method to solve for your BMI.
    metric_Weight = float(input("What is your weight(kg)?"))    #This prompts the user to input their own weight(kg).
    metric_Height = float(input("What is your height(metres)?"))    #This prompts the user to input their own height(metres).
    metric_BMI_numerator = (metric_Weight)  #The formula is equal to the weight divided by the height sqaured. This is the numerator of the formula.
    metric_BMI_denominator = (metric_Height**2)#This is the denominator of the formula. 
    metric_BMI_calculator = (metric_BMI_numerator/metric_BMI_denominator)   #The BMI calculator variable will take the numerator divided by the denomiator
                                                                            #to get the final BMI.
    
    if metric_BMI_calculator < 18.5:    #If the BMI is less than 18.5, it will display that the user is underweight. 
        BMI_statement = ("underweight")

    if metric_BMI_calculator >= 18.5 and metric_BMI_calculator <= 25:   #If the BMI is between 18.5 and 25, it will display that the user is normal.
        BMI_statement = ("normal")

    if metric_BMI_calculator > 25 and metric_BMI_calculator < 30:   #If the BMI is over 25 but less than 30, the user is overweight.
        BMI_statement = ("overweight")

    if metric_BMI_calculator >=30:  #If the BMI is 30 and over, the user is obese.
        BMI_statement = ("obese")
        
    print("""%s, with a height of %i metres and a weight of %i kilograms, you have a BMI of %.2f. This is considered %s."""%
(user_Name, metric_Height, metric_Weight, metric_BMI_calculator, BMI_statement))
    #This will give the final statement, by outputting the user's name, their weight in kg, their height in metres, their final BMI and a final statement of
    #their index (underweight,normal, overwieght or obese).

