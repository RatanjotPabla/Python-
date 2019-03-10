#Name:              Ratanjot Pabla
#StudentNo:         32700826
#Date_Submitted:    October 12, 2018
#File_Name:         purchaseDiscountAssign3.py
#Teacher_Name:      Mr. Sarros
#Purpose:           This program will ask the user for their purchase total. If the program reads that the user has purchased over 10 dollars, they will be given a
                    #10 percent discount. Then the program will output the sub-total, the tax amount by outputting 13 percent of the sub-total, and finally
                    #adding the taxes onto the sub-total and outputting their final total. 

purchase_Amount = float(input("What is your purchase total for today")) #This prompts the user for their total purchases at their store.
print("Purchase:        $%.2f"%(purchase_Amount))   #This will print out the customer's purchase at their store. 

if purchase_Amount > 10:    #If the purchase is greater than 10 dollars, it will follow the true branch, otherwise, it will follow the false branch.
    discount_Amount = (purchase_Amount * 0.1)   #Once it sees the purchases being over 10 dollars, the discount_Amount variable will calculate the discount by
                                                #multiplying the total purchases by 0.1 since the discount is 10%.
    sub_Total= (purchase_Amount-discount_Amount)    #The subtotal is equal to the total purchases minus the discount.
    tax_Amount = (sub_Total * 0.13) #The taxes is equal to the subtotal (the variable above) times 0.13 to figure out 13 percent of the subtotal.
    total_Amount = (tax_Amount+sub_Total)   #The total amount is equal to the tax amount added to the subtotal.
    
    print("Discount:        $%.2f"%(discount_Amount))   #This will print out the customer's discount after their total purchases.
    print("Sub-Total:       $%.2f"%(sub_Total)) #This will print out the customer's subtotal after the discount deductions. 
    print("Tax(13 percent): $%.2f"%(tax_Amount))    #This will print out the customer's tax from the customer's subtotal.     
    print("Total:           $%.2f"%(total_Amount))  #This will print out the final total after the discount and the taxes.
    print("Your final total for today after the discount and taxes at our store is $%.2f."%(total_Amount))  #This will print out a final statement of your total.

    
else:   #If the customer hasn't purchased anything over ten dollars, it will follow the same code as above but without any discount deductions.
    non_discounted_taxAmount = (purchase_Amount*0.13)   #Instead of finding 13 percent of the subtotal which has the discount(10%) on it from the true branch, this will
                                                        #find 13 percent of the purchase amount. 
    non_discounted_totalAmount = (purchase_Amount+non_discounted_taxAmount) #The total amount is equal to 13 percent of the purchase total plus the purchase total.
    print("Discount:        $0.00") #Since the purchase is under 10 dollars, the discount is 0 dollars. 
    print("Sub-Total:       $%.2f"%(purchase_Amount))   #The subtotal is the same as the purchase amount since there are no discount deductions on it. 
    print("Tax(13 percent): $%.2f"%(non_discounted_taxAmount))  #This will print out the tax of the purchase total. 
    print("Total:           $%.2f"%(non_discounted_totalAmount))    #This will print the final total after the taxes on the customer's purchases. 
    print("Your final total for today after taxes at our store is $%.2f."%(non_discounted_totalAmount)) #This will print out a final statement of your total.
          
    
          
    

