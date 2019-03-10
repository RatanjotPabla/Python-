#Name:      Ratanjot Pabla
#StudentNo: 32700826
#Date:      October 10, 2018
#File_Name: stateFairContest.py
#Teacher:   Mr. Sarros
#Purpose:   This program is an example of an if else statement. The following program will
            #prompt the user for their name and their weight. If their weight is between the range of 85 lbs to
            #115 lbs, then the contestant can qualify to enter the heavyweight division. If not, then they can't
            #qualify for the contest. 

Contestant_Name= input("What is your name?")    #This prompts the user to input their name.
Contestant_Weight=float(input("What is your weight(lbs)?")) #This prompts the user to input their weight in pounds(lbs).

if Contestant_Weight >= 85 and Contestant_Weight <= 115:
    print ("You are qualified to enter into the contest with a weight of %.f pounds, %s."%(Contestant_Weight,Contestant_Name))  #If the program reads that the
    #If the program reads that the contestant's weight is between 85 pounds and 115 pounds, the true branch will output that the user is qualified for the contest.
else:
    print("""You are not qualified to enter into the contest. To enter the contest, your weight must be between 85 to 115 pounds.
Your actual weight is %.f pounds, %s."""%(Contestant_Weight,Contestant_Name))
    #If the program reads that the contestant is not between the weight range, then it will output the false branch saying that the user is not qualified for the 
    #contest.
