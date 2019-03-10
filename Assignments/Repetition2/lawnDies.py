#Name:              Ratanjot Pabla
#StudentNo:         32700826
#Date_Submitted:    October 26, 2018
#File_Name:         lawnDies.py
#Teacher_Name:      Mr. Sarros
#Purpose:           This program will determine how many days it will take for fifty percent of the lawn to die, if each day, it dies by six percent. Also, the given
                    #area of the lawn is 100 units. In other words, how many days it will take to have fifty units of grass to remain alive.
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------


days=0                                  #The variable name, 'days,' is assigned the value of 100.

for lawn_Amount in range (100,50,-6):   #A for loop for the lawn_Amount in range (100,50,-6). The sequence underneath will follow from the range of 100 to 50 in the
                                        #lawn_Amount as it is subtracting 6 in each iteration from the 6 percent of grass dying per day. 

    if lawn_Amount > 50:                #If the lawn_Amount doesn't reach to exact fifty and is over fifty because of a remaindr left from subtracting 6 each time;
                                        #the lawn_Amount will subtract 6 units each time.
        lawn_Amount -=6                 
    days+=1                             #As well as the lawn_Amount subtracting 6 each time, the days will add by one each time, to figure out how many days it took.
print(days)                             #Print statement of how many days it took for the lawn_Amount of 100 units to reach half the amount.
print(lawn_Amount)
    
