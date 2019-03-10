#Name:      Ratanjot Pabla
#StudentNo: 32700826
#File_Name: pythonBasicsAssignment2.py
#Teacher:   Mr. Sarros
#Purpose:   This program will ask the user for their input and output it, will input and output the user's birthdate, show the use of all six mathematical
            #operations, output the surface area of a cube once a side length has been inputted. Finally, it will output a number that had been rounded by
            #two numbers. 


name = input("Enter your full name:")                                   #The first program asks the user for their full name. It will later output it. 
print("Thanks", name+".")

BirthDate = input("\nEnter your birthdate(yyyy/mm/dd):")                #The second program asks the user for their birthdate. It will later output it.
print("Your birthday is on", BirthDate+ ". Nice to know!")

for x in range(1,10):
    print()

print("\nMoving onto number two, we will demonstrate the use of all six math functions.")    #The third program showing the six mathematical operations.
Power = print("\nThe first operation is the exponentiation which sqaures the base number. For an example, 5**2 is equal to", 5**2.)#Power operation 
Multiplication = print("\nThe second operation is multiplication. For an example, 2*3 is equal to", 2*3.)#Multiplication operation 
Division= print("\nThe third operation is division. For an example, 14/3 is equal to", 14/3)#Division operation
Remainder = print("\nThe fourth operation is remainder. This will divide the two numbers and output a number that displays the remaining numbers after closest quotient. For an example, 14%3 is equal to", 14%3)
#Remainder operation

Addition = print("\nThe fifth operation is addition. For an example, 1+2 is equal to", 1+2)#Addition operation
Subtraction = print("\nThe final math operation is subtraction. For an example, 4-3 is equal to", 4-3)#Subtraction operation 

for y in range(1,10):
    print()
print("Moving onto number three, we will calculate the surface area of a cube")#The fourth program outputting the surface area of a cube. 
SurfaceArea = int(input("What is the length of the edge of the cube?"))#Asks the user to input the lenght of one of cube's edges. 
SA = (SurfaceArea*SurfaceArea)*6#Solves the surface area of the cube by squaring the edge length and multipliying it by six for the final answer.
print("The surface area of your cube is", SA,"units squared.")#Outputs the surface area. 

for z in range(1,10):
    print()
print("On to the final program, we will show you how to round off your real number to two decimal places using the round function. For an example, 14/3 is equal to 4.6666666667 but when you use the round fucntion, it will be equal to")
print(round(14/3,2))#The fifth program will take the answer to the division equation and round it to two decimal places.






