#Name:          Ratanjot Pabla
#Student:       32700826
#FileName:      Ratanjot_Pabla_Text-BasedConnectFour_FSE.py
#Date:          January 08, 2019
#Teacher:       Mr.Sarros
#Purpose:       This program will be used to create a two-player Connect Four game using the numpy, sys, time and math libraries. Along with the tkinter and
                #pygame GUI modules. The motive of the game is for one of the player to connect four pieces of the game board in a row(either vertically, horizontally,
                #or diagonally). The program will check if a player has connected four pieces in a row. Once it does detect this, the game will end and one of
                #players has won. Before playing, players will be given the option to look at the user guide instructions on what the game is and how to play the game. 
                

#Numpy is a python library; well sufficient to support large, multi-dimenstional arrays and matrices. This library helps the arrays by
#consisting a large collection of high-level mathematical operations as well.
import numpy as np                  
from tkinter import*
import time



def game():
    Row_Amount  = 6     #The gameboard has six rows.
    Column_Amount = 7   #The gameboard has seven columns.


    def create_gameboard(): #Creation of the connect four gameboard using arrays of zeros to display the number of rows and columns of the entire board.
        gameboard = np.zeros((Row_Amount,Column_Amount))    #In the brackets are a tuple of values to specify the shape size in terms of how many zeros per array 
        return gameboard                                    #and how many arrays there in total. By default the data type of the function will be a float; regardless of
                                                            #specification in parenthesis.

    def drop_pieces(gameboard, rows, columns, pieces):  #For whenever the player clicks on the board in a column, this will fill in the board with whatever piece  
        gameboard[rows][columns] = pieces               #the player had dropped in 

    def available_slot(gameboard, columns):             #If this command is ran and it is true then this allows for the player to drop a piece.
        return gameboard[Row_Amount-1][columns] == 0    #If it is not true then this doesn't allow for the player to drop a piece as the program sees if all the slots
                                                        #in the column have been taken up.


    def next_open_row(gameboard, columns):              #Whenever a piece has been dropped, the program is coded in a way so that the piece has been dropped into the nearest row.
        for r in range(Row_Amount):                     #Going back to how we had used numpy to create our board, if the board reads a zero in a row within the column, it will return
            if gameboard[r][columns] == 0:              #that zero.
                return r

    def print_board(gameboard): #Another numpy function so that when we click for our pieces to be inserted into the board, the pieces fall from bottom to top
        print(np.flip(gameboard, 0))    #instead of from top to bottom if we didn't have the flip function for the gameboard.


    def winning_move(gameboard, pieces):
        # Check horizontal locations for win(This will start checking from the most left of the four pieces connected)
        for c in range(Column_Amount-3):    #Three columns are subtracted since three columns from either ending sides of the board will not make a horizontal win.
            for r in range(Row_Amount): #The if statement will check if their are four pieces in the same row but with the columns four apart from each other.
                if gameboard[r][c] == pieces and gameboard[r][c+1] == pieces and gameboard[r][c+2] == pieces and gameboard[r][c+3] == pieces:
                    return True
       

        # Check vertical locations for win(This will start checking from the most bottom of the four pieces connected)
        for c in range(Column_Amount):  #Three rows are subtracted since three rows from either top or bottom of the board will not make a vertical win.
            for r in range(Row_Amount-3):   #The if statement will check of their are four pieces in the same column with the rows four apart from each other.
                if gameboard[r][c] == pieces and gameboard[r+1][c] == pieces and gameboard[r+2][c] == pieces and gameboard[r+3][c] == pieces:
                    return True

        # Check positively sloped diaganols(This will start checking from the bottom left hand corner of the four pieces connected)
        for c in range(Column_Amount-3):    #Three columns are subtracted since three columns in the corners within three rows will not make a diagonal win.
            for r in range(Row_Amount-3):   #Three rows are subtracted since three rows in the corners within the three columns will not make a diaginal win.
                if gameboard[r][c] == pieces and gameboard[r+1][c+1] == pieces and gameboard[r+2][c+2] == pieces and gameboard[r+3][c+3] == pieces:
                    return True #The positive diagonals check for a row of four with a column and row being increased each time.


        # Check negatively sloped diaganols(This will start checking from the top left hand corner of the four pieces connected)
        for c in range(Column_Amount-3):    #Three columns are subtracted since three columns in the corners within three rows will not make a negative slope diagonal win.
            for r in range(3, Row_Amount):  #THe rows must start at three since you cannot connect four pieces within rows from 4-6. The last row you can win from is row 3
                if gameboard[r][c] == pieces and gameboard[r-1][c+1] == pieces and gameboard[r-2][c+2] == pieces and gameboard[r-3][c+3] == pieces:
                    return True #The negative diagonals check for a row of four with a row being decreased, whilst a column is being incresed each time.

        

    def destroy(): #Will destroy the start screen window and proceed with the game
        root.destroy()
     
        
        

    def userguide():    #User guide screen. Displays the instructions and controls for the game.
        top=Toplevel()
        top.title("USER GUIDE")
        top.geometry("1366x768")
        top.configure(background="red")
        user_guide_title = Label(top, text = "USER GUIDE", relief = "flat", bd = 10, bg="black", fg="white",font = "Verdana 40")
        user_guide_title.place(x=500,y=10)
        user_guide_1 = Label(top, text = """You've reached the page where we will talk about the instructions and controls of the game.
        This is a Two-Player Connect Four Game.""", relief = "ridge", bd = 10, bg = "white",fg = 'blue',font ="Times 18")
        user_guide_1.place(x=200,y=150)

        user_guide_2 = Label(top, text = """Player 1 will be representing the number '1' on the game board and player 2 will be
        representing the number '2' on the game board. The incentive behind this game is for one of the players to connect four
        of their own numbers in a row. This could be either horizontally, vertically or diagonally. The game will start off with
        player 1; once player 1 has gone, it will be player 2's turn to put in their number. In order for the players to make their
        selection, they must type in the number of the column; ranging from 1-7 where number '1' is representing the first column
        of the game board, number '2' is representing the second column and so on until the seventh column."""
        ,relief = "groove", bd = 10, bg = "white",fg = 'blue',font ="Times 18")
        user_guide_2.place(x=80,y=250)
        user_guide_3 = Label(top, text = "CALL YOUR FRIEND RIGHT NOW AND LET THE GAME BEGIN.",relief = "groove", bd = 10, bg = "white",fg = 'blue',font ="Times 30")
        user_guide_3.place(x=125,y=450)
        user_guide_Exit = Button(top, text ="BEGIN TO PLAY (CLICK HERE)",bg = "yellow",fg = "blue",command = destroy,font ="Verdana 25")
        user_guide_Exit.place(x=150,y=600)


    def countdown(time):    #Used as a command for the load up screen.  
        if time == 0:   #When the initial time from 5 seconds goes all the way to 0 seconds, the load up screen will close and the game will start.
            countdown_window.destroy() 
        else:   
            label.configure(text="Please Wait While Your Game Is Loading.\n\n Ratanjot Pabla Presents To You...", relief = "groove", bd = 10,
                            bg = "PeachPuff",fg = 'blue', font = "Verdana 20 bold underline")
            countdown_window.after(1000, countdown, time-1)
            #During the time period from when the time is going down by one second each time from 5 seconds to 0 seconds, a label will be displayed
            #telling users to wait for the game to load.
            


            
    countdown_window = Tk() #Creates a new window for the load up screen
    label = Label(countdown_window, width = 50, height = 15)    #Creates a label. Mainly used for the dimensions of the window so that you could have symmetrical 
    label.pack(padx=30, pady=30)                                #borders from each corner of the text using the padx and pady function.
    countdown(3)    #Countdown is set to five seconds.
    countdown_window.mainloop() #GUI ends off with a mainloop method.

      

    root = Tk()
    root.title("Connect Four")  #title of start screen window
    root.geometry("1366x768") #set size of start screen window
    root.configure(background="red", relief = "raised", bd = 20) #set start screen window's background colour
    game_title = Label(root,borderwidth = 3, bg = "red",text = "CONNECT FOUR!!!",font ="Times 64 bold underline").pack()    #Label for game title("CONNECT FOUR!!!")




    PLAYER_1 = Label(root,relief = "solid", text = "PLAYER 1 REPRESENTS NUMBER:", font = "Times 16")    #Label for informing the audience what number
    PLAYER_1.place(x=50, y=250)                                                                         #player 1 represents('1'). Along with the positioning
    PLAYER_1_NUMBER = Label(root,relief = "raised", text = "'1'", bg = "black", bd = 15, fg="white", font = "Verdana 100")
    PLAYER_1_NUMBER.place(x=150, y=300)

    PLAYER_2 = Label(root,relief = "solid", text = "PLAYER 2 REPRESENTS NUMBER:", font = "Times 16")    #Label for informing the audience what number
    PLAYER_2.place(x=950, y=250)                                                                        #player 2 represents('2').
    PLAYER_2_NUMBER = Label(root,relief = "raised", text = "'2'", bg = "black", bd = 15, fg="white", font = "Verdana 100")
    PLAYER_2_NUMBER.place(x=1050, y=300)




    #Creates a button. Once clicked, it will follow the command called play where the screen will close up and the game will begin. Along with the positioning.
    playButton = Button(root,text = "PLAY", bg = "yellow",fg = "blue",command = destroy, font = "Times 40")
    playButton.place(x=580,y=200)

    #Creates a label to inform the audience that the game starts with player 1 as to who goes first. Along with the positioning.
    playButton_label = Label(root,relief = "ridge", text = "THE GAME STARTS WITH PLAYER 1", bg = "black", bd = 5, fg="white", font = "Times 10")
    playButton_label.place(x=560,y=310)




    #Creates a button. Once clicked, it will follow the command called userguide where another window will pop to show the game's information. Along with the positioning.
    userguide_Button = Button(root,text = "USER GUIDE", bg = "yellow", fg = "blue",command=userguide, font = "Times 40")
    userguide_Button.place(x=500,y=460)

    #Creates a label to inform that the user guide button is meant to get more details and controlling information on the game. Along with the positioning.
    userguide_Button_label = Label(root,relief = "ridge", text = "FOR DETAILS AND CONTROLS", bg = "black", bd = 5, fg="white", font = "Times 10")
    userguide_Button_label.place(x=585,y=570)

    #Every GUI must end with a mainloop method.
    root.mainloop()



    gameboard = create_gameboard()  #Creation of the board to actually have the player's input of their pieces into a variable(gameboard)
    print_board(gameboard)
    game_over = False   #This variable is used to have the game loop on forever until it becomes true.  
    player_turn = 0     #This will navigate through the player's turn(either player 1 or 2). To do so, the player_turn variable accumumlates the players turn by adding
                        #one each time to the variable. If we see that the accumulation is divisible by two without a remainder, then it is player's one turn. If not,
                        #then it will be player two's turn.(EX: 7/2 = 3.5 (player two's turn))

    count = 0           #Variable count is assigned a value of zero where it will be used to accumlate the number of turns there have been in total throughout each game.       




       
    #Game will loop until the game is equal to variable game_over (game_over = False). If it is true, then the game will be over. This is either by a player
    #winning four in a row or if their is a draw in the two player's match.
    while not game_over:
        if player_turn == 0:    #If player_turn is equal to zero then it will prompt player 1 with the number of the column for where they wish to insert their piece.
            columns = int(input("Player 1, make your selection(type a digit from 1-7 that represents the number of the column):"))
            columns = columns-1     #When the program takes the column number, the indexing of the program starts with the first column having the index of 0. So, when 
                                    #the player returns us with the number of the column, we must subtract one from it to navigate the same column to the proper index.

            count +=1               #Accumlates to count by adding one each time. This is used to count how many turns the program has gone through between both
                                    #players. Once the count variable has the value of 42, this must mean that game is a draw since all 42 slots have been taken up
                                    #without a winner.

           
     

            #When player one inserts a piece into the gameboard through a column, the program will make sure that the column is still available with empty slots.
            if available_slot(gameboard,columns):   
                rows = next_open_row(gameboard, columns)    #This will take the next empty row for the player to place in within the column of the gameboard.
                drop_pieces(gameboard, rows, columns, 1)    #This will drop player one's piece into the gameboard, taking in the information of what row and column has
                                                            #been taken up.

                #If four pieces have been connected in a row(either horizontally, vertically, or diagonally), the game will stop and show that player 1 has won. 
                if winning_move(gameboard, 1):  #This shows if winning move has four pieces connected together by player one from the possible patterns. The game must end.
                    game_over = True    #It is true that the game is now over.
                    victory1_window =Tk()   #Creates a new window to display player one's victory.
                    victory1_window.geometry("1366x768")    #Sets the dimensions of the window.
                    victory1_window.configure(background="red") #Sets the background colour of the window as red.

                    #Creates a label for player 1 that they have won (PLAYER 1 WINS\n CONGRATULATIONS!!!) in a stylistic font. Along with the positioning.
                    player1_winner = Label(victory1_window,borderwidth = 3, bg = "red",text = "PLAYER 1 WINS\n CONGRATULATIONS!!!\n Play again using Python Shell Window.",font ="Times 50 bold underline")
                    player1_winner.place(x=130,y=200)
                    victory1_window.after(4000,victory1_window.destroy) #After four second of displaying the screen, it will destroy it and prompt the user if they wish 
                    victory1_window.mainloop()                          #to exit out of the Python Shell window which they were playing in.
                    
                    


       
                
                    
                    
    #PLAYER 2                
                    

        else:   #The code following under the else statement is similar to the code above for player 1. This code has some adjustments made for player 2.
            columns = int(input("Player 2, make your selection(type a digit from 1-7 that represents the number of the column):"))
            columns = columns-1
            count+=1


            #A set of program to check if the player's column choice is still available. Which will then follow by the player dropping the piece into the gameboard
            #of the nearest empty row. For more information, look at the same portion of this code but for when it's player one's turn above.
            if available_slot(gameboard,columns):
                rows = next_open_row(gameboard, columns)
                drop_pieces(gameboard, rows, columns, 2)


            
                #A set of program to output player two's victory. For more information, look at the same portion of this code but for when it's player one's turn above.
                if winning_move(gameboard, 2):
                    game_over = True
                    victory2_window =Tk()
                    victory2_window.geometry("1366x768") 
                    victory2_window.configure(background="yellow")
                    player2_winner = Label(victory2_window,borderwidth = 3, bg = "yellow",text = "PLAYER 2 WINS\n CONGRATULATIONS!!!\n Play again using Python Shell Window.",font ="Times 50 bold underline")
                    player2_winner.place(x=130,y=200)
                    victory2_window.after(4000,victory2_window.destroy)
                    victory2_window.mainloop()
                    
                   

        #A set of program to check if their is a draw in the game. For more information, look at the same portion of this code but for when it's player one's turn above.
        if count == 42: 
            draw_window =Tk()
            draw_window.geometry("1366x768") 
            draw_window.configure(background="red") 
            draw = Label(draw_window,borderwidth = 3, bg = "red",text = "DRAW\n NOBODY WINS THIS ROUND!!!\n Play again using Python Shell Window.",font ="Times 50 bold underline")
            draw.place(x=130,y=200)
            draw_window.after(4000,draw_window.destroy)
            draw_window.mainloop()
            game_over = True
            



        
            
                    
        print_board(gameboard)  #Each time a player has made a column selection, the output will be an updated version of how the game board looks like thus far.
        player_turn += 1        #Acuumulates the player's turn by adding 1 to the variable player_turn each time.
        player_turn = player_turn % 2   #If the accumulation of player_turn sees that the accumulation number is divisible by two without a remainder then it must be
                                        #player one's turn. Whereas, if the program sees that the accumulation number is not divisible and that their is a remainder, then
                                        #it must be player two's turn.



def main():
    game()  #The define function "main" will run the game first. Once either player has won or the round is a draw, the players will be prompted if they wish to play 
    while True: #once more. If they do, then the game will restart but if they say no then the game will end. 
        restart = input("Would you like to play again? Please enter 'y' for YES or 'n' for NO: ")
        restart = restart.lower()
        if restart == "y":
            game()
        else:
            print("Thanks for playing")
            quit()
			   
main()  #The initialization of what starts and runs the game in a loop.

