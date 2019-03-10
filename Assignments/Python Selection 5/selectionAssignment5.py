#Name:              Ratanjot Pabla
#StudentNo:         32700826
#Date_Submitted:    October 17, 2018
#File_Name:         selectionAssignment5.py
#Teacher_Name:      Mr. Sarros
#Purpose:           This program is used to help the driver decide if they will need to get gas or if they will
                    #make it with the amount they have left. We must calculate the tank capacity, gas gauge and the highway MPG to solve for the total
                    #miles they can travel or require and the gallons they have left or rquire to travel the full 200 miles until the next gas station. 

tank_Capacity = float(input("What is the capacity of the gas tank, in gallons?"))   
    #This will prompt the user for their gas tank capacity in gallons.

gas_Gauge = float(input("What is the indication of your gas gauge in decimal? (Ex: 50% is equal to 0.5)"))
    #This will prompt the user for their gas gauge in decimal.

highway_MPG = float(input("What is the miles per gallon your car achieves on the highway?"))
    #This will prompt the user for their MPG of their car they achieve on the highway.

miles_Total = (highway_MPG*tank_Capacity*gas_Gauge) #This tells you how many miles you can travel in total
miles_Left = (miles_Total-200)  #This does the calculation of the number of miles you have left after travelling the full 200 miles.
miles_Required = (200 - miles_Total)    #This does the calculation of the number of miles you need more to reach the full 200 milles. 
gallons_Left = (tank_Capacity-(200/gas_Gauge/highway_MPG)) 
    #This will do the calculation of finding out the number of gallons you have left after travelling the full 200 miles.

gallons_Required = ((200/gas_Gauge/highway_MPG)-tank_Capacity)
    #This will do the calculation of the number of gallon they require more to reach the full 200 miles. 

if miles_Total>= 200:
    print("""Safe to proceed. You can cross the 200 miles with %.2f remaining miles to travel in the tank. You also have %.2f gallon(s) left"""%
(miles_Left,gallons_Left))
    #If the car can travel the full 200 miles and and have gas left over, this will print out that it is safe to proceed. It will also print out that
    #the remaining of miles they have left that they can travel until they have an empty tank and the number of galllons they have left over. 

else:
    print("""Get gas. You will be able to travel only %i miles and will need enough gas to travel another %.2f until the next gas station. You will
need another %.2f to reach the full 200 miles."""%(miles_Total,miles_Required,gallons_Required))
    #If the car can not travel the full 200 miles, it will print out to the user that they must get gas. It will also print out the number of miles they
    #are short by to reach the full 200 miles and also the number of gallons they require to reach the full 200 miles.
    
                    
