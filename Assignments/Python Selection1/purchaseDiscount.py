#Name:          Ratanjot Pabla
#StudentNo:     32700826
#Date:          Ocotber 02, 2018
#File_Name:     purchaseDiscount.py
#Teacher:       Mr. Sarros
#Purpose:       This program will ask the user to input their total purchases. If their total is over 100 dollars, they will be given a 25 percent discount.
                #Whereas, if the total is not over 100 dollars, their purchases will stay the same.

Amount = float(input("What is your total for today?")) #This asks the user to input their total purchases for that day. 

if Amount>= 100.01:
    print("Your total amount comes down to $%.2f. Thank you. Come again"%(Amount*0.75)) #If the amount is $100.01 or over, the amount will be given a 25% discount                                                                                    
                                                                                        #as shown in the true branch and output the final total.
else:
    print("Your total comes down to $%.2f. Thank you. Come again."% (Amount))           #If the amount is $100 or under, the amount will remain the same. 
    
