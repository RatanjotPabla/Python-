#Name:              Ratanjot Pabla
#StudentNo:         32700826
#Date_Submitted:    October 25, 2018
#File_Name:         acronym.py
#Teacher_Name:      Mr. Sarros
#Purpose:           This program is used to output an acronym of a title which the user inputs within a while loop. The user must type in each of the words in the
                    #title seperately until he gets to the last word of the title, to which he must type, "end." This program also ignores the words,
                    # "the", "of" and "and." After each word is typed, it grabs the first letter of each word and capitalizes it. Then once the user types, "end",
                    # the program will input a period in between each letter. Hence, creating your very own acronym.
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
acronym = ""  #variable "acronym" is equal to an empty space.

while True: #While True loop.
    
    word = input("Enter your title(one word at a time): <end to exit>")   #Prompts the user to input their title by inputting one word at a time.  
    word = (word.replace('the','').replace('of','').replace('and',''))    #This replaces the words, "the", "of" and "and" with an empty space.
    

    if word != "end":    #If Acronym is not equal to "end" it will follow the program underneath.
        word = (word[:1]) #The variable "word" is equal to the first letter of each word.
        acronym+= word.upper() #Each letter is accumulated together and capitalized. 
                        
    else:   #Once the user types "end," it will follow the program underneath.
        acronym = acronym.replace('','.')   #This replaces each empty space in the acronym with a period in between.
        print(acronym[1:])    #The program prints the acronym starting from the index position 1 to the end of the acronym since the first character is a period. 
        break    #To stop the program from continuing the while loop.
    
        
    

    
        

   


        
       

        
    
