#Name:              Ratanjot Pabla
#StudentNo:         32700826
#Date_Submitted:    November 19, 2018
#File_Name:         listAssign2Q2.py
#Teacher_Name:      Mr. Sarros
#Purpose:           This program will allow for two people to play a dice game called PIG. The objective of the game is to be the first player to reach 100 points.
                    #On a turn, a player rolls the die repeatedly until either a one is rolled or if the player chooses to hold their turn(stop rolling).
                    #If a one is rolled, that player's turn ends and their accumulated points will be zero. If the player chooses to hold, then all the points during
                    #their turn will be added upon their score. Once ther first player reaches 100 or more points, the game end and that player is the winner. The
                    #following program will include the usage of the '.randint()' function to output a random number from 1 to 6 when the player rolls the die.

import random   #Importing the random function
x = 0
accum_One = 0
accum_Two = 0

while True:
    player1 = random.randint(1,6)   #Each roll for player one is assigned to a random number between 1 to 6. 
    print("\nPLAYER 1:\nThe number you rolled was",player1) #Prints player one's roll. 
    accum_One = accum_One + player1     #Accumulates the total points for player one.
    if accum_One >= 100:    #If playeer one scores greater than or equal to 100 points, then they will be the winner. 
        print("You got %i points.\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!PLAYER 1 WINS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"%(accum_One))
        break
    if player1 != 1:    #If the player doesn't roll a one, it will follow continue by asking if the player wants to hold or continue their turn.  
        Hold_One = input("\nHello player 1. Would you like to hold or continue? Press 'h' to hold or 'c' to continue.\n")
        
        if Hold_One == 'h': #If the person types in 'h' for hold, it will go to player two.  
            print("\nYour total points add up to %i so far. It is now your opponent's turn.\n----------------------------------------------"%(accum_One))
            
            while x != 1:
                player2 = random.randint(1,6) #Each roll for player two is assigned to a random number between 1 to 6. 
                print("\nPLAYER 2:\nThe number you rolled was",player2) #Prints player two's roll. 
                accum_Two = accum_Two + player2     #Accumulates the total points for player two. 
                if accum_Two >= 100:    #If playeer two scores greater than or equal to 100 points, then they will be the winner.
                    print("You got %i points.!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!PLAYER 2 WINS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"%(accum_Two))
                    break
                if player2 != 1:    #If player two does not get a one on their roll, then they will be asked to either hold their turn or continue. 
                    Hold_Two = input("\nHello player 2, would you like to hold or continue? Press 'h' to hold or 'c' to continue.\n")
                    if Hold_Two == 'h':    #If player two inputs 'h' for hold, then player two's turn will break and it will go back to player one again
                        print("\nYour total points add up to %i so far. It is now your opponent's turn.\n----------------------------------------------"%(accum_Two))
                        break   #This will output player two's total points so far and will then break right after. 
                if player2 == 1:    #If player two rolls a one on their turn then it will follow the sequence of orders below. 
                    accum_Two = 0   #This will make the accumulated points restart back to zero 
                    print("Your accumulated points will restart to %i. It is now your opponent's turn.\n--------------------------------------------------"%(accum_Two))
                    break   #Print statement for the accumulated points restarting back to zero, followed by a break and will return to player one's turn. 
                    
        
    else:   #If the player rolls a one during their turn, then it will follow the sequence of orders below.
        accum_One = 0   #The accumulated points will restart back to zero and it will be player two's turn. 
        print("Your accumulated points will restart to %i. It is now your opponent's turn.\n--------------------------------------------------"%(accum_One))
        while x != 1:
            player2 = random.randint(1,6)   #Each roll for player two is assigned to a random number between 1 to 6. 
            print("\nPLAYER 2:\nThe number you rolled was",player2) #Prints player two's roll. 
            accum_Two = accum_Two + player2     #Accumulates the total points for player two.   
            if accum_Two >= 100:    #If player two scores greater than or equal to 100 points, then they will win. 
                print("You got %i points.\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!PLAYER 2 WINS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"%(accum_Two))
                break   #Player two wins and the game ends after the break statement. 
            if player2 != 1:    #If the player does not roll a one then they will be asked to either hold or continue their turn. 
                Hold_Two = input("\nHello player 2, would you like to hold or continue? Press 'h' to hold or 'c' to continue.\n")
                if Hold_Two == 'h':     #If player two decides to hold, then it will output their total points thus far.
                    print("\nYour total points add up to %i so far. It is now your opponent's turn.\n----------------------------------------"%(accum_Two))
                    break   #Breaks player two's turn and will go to player one's turn.
            if player2 == 1:    #If player two rolls a one, then it will go back to player one's turn to roll the die.
                accum_Two=0     #Player two's accumalted points will restart down to zero.
                print("Your accumulated points will restart to %i. It is now your opponent's turn.\n--------------------------------------------------"%(accum_Two))
                break   #This will break player two's turn and it will go back to player one's turn. 
                

            
#Line 18-25: This is the program used for player one during their turn.
#Line 27-48: This is the program for player two when player one holds their turn. 
#Line 51-72: This is the program for player two when player one rolls a one on their turn.




































                
