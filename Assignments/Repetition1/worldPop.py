#Name:              Ratanjot Pabla
#StudentNo:         32700826
#Date_Submitted:    October 25, 2018
#File_Name:         worldPop.py
#Teacher_Name:      Mr. Sarros
#Purpose:           This program is used to see how many years it will take for the current population to reach a population twice the current population if the
                    #population increases by 1.11% per year. We must use a while loop to do so.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

current_Population = (6.875*10**9)  #The value of the current population (6875000000).
rate= 1.0111    #The value of the increasing rate in population per year. 
total=0     #The total value is assigned the value of 0 for now.
count=0     #The count value is also assigned a value of 0.
final_Population=(current_Population*2) #The final population that we are trying to find out the number of years it will take to get to is, the "current_Population*2".


while current_Population<final_Population:  #While the current_Population is less than the "final_Population."
    current_Population=(current_Population*rate)    #The "current_Population" is equal to the current_Population times the increasing rate(1.11%). 
    total+=current_Population   #This will continuosly equal to the sum of the previous "current_Population" to the newer "current_Population" after each year. 
    count+=1    #The counter to see how many years it will take to reach double the population is equal to 1 added to the "count" for each new year.
    
print("""If the increasing rate each year is 1.11 percent, then it will take %i years for the current population to double. The population after %i years
will be %.2f."""%(count,count,current_Population))  #Finally, when the program sees that the current_Population is no longer less than the "final_Population", it
                                                    #will output how many years it has taken and the population of that exact year. The number of years(63) may not
                                                    # be exactly equal to the "final_Population"(it can be exact or higher). Therefore, we must see what the population
                                                    #is equal to in that year. In other words, the 62nd year was lower than final_Population and the 63rd year was
                                                    #greater than the final_Population; meaning it took between 62-63 years to reach the "final_Population."


