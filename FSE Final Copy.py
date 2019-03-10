#The following program asks the user 40 total math questions.
#The game will ask the user which math operation they will want to try for each round until the last round begins.
#The operations the program uses are addition, subtraction, multiplication and division.
#Once you choose one operation, you will be asked ten questions, then choose another operation that is remaining. You will do this until the end.
#Once you reach the last operation, you will be automatically asked ten questions of the last operation. Then it will output your mark out of forty
#displaying if you can do better next time or not. 

import random  
print()                                                                              #Game Title
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Train Your Cranium!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print()
print()
print()
start = int(input("Type '1' for instructions.\nType '2' to play."))                   #The main menu displaying a button to show inastructions and a button
                                                                                      #start playing.
if start == (1):
    print()
    print("This is the one and only game that will test your numeric math skills.")    #If you press one, it will display all the instructions.
    print("All you need to do is select which operation you would like to play first to start.")
    print("The four operations you get to choose from are addition, subtraction, multiplication and division.")
    print()
    print("Once you choose one operation, you will be asked ten questions back to back using that operation and you can't select the operation again in the next round.")
    print("You will have to choose the remaining operations that you haven't chosen.")
    print("Once you are on the fourth round, you will be asked ten questions from the only remaining operation left automatically. Now, it's time to play,'Train Your Cranium'!")
    print()
elif start == (2): #If you press two, it will display the outputs of what operation you will like to try first. 
    print()
game = input("\nType in an operation sign to begin.\n(+) - for addition.\n(-) - for subtraction.\n(*) - for multiplication.\n(/) - for division.")
print()


            


mark = 0 #All the marks from each round. For each new round, the next mark variable will start. For every questions right, your mark will gain by one.
mark1 = 0 #If you get the question wrong, the mark will remain the same. At the very end, all mark variables will be added to get a sum out of forty.
mark2 = 0
mark3 = 0


question = 0 #All possible 64 questions in the pseudo code, based on the possible variations of questions asked. 
question1 = 0
question2 = 0
question3 = 0
question4 = 0
question5 = 0
question6 = 0
question7 = 0
question8 = 0
question9 = 0
question10 = 0
question11 = 0
question12 = 0
question13 = 0
question14 = 0
question15 = 0
question16 = 0
question17 = 0
question18 = 0
question19 = 0
question20 = 0
question21 = 0
question22 = 0
question23 = 0
question24 = 0
question25 = 0
question26 = 0
question27 = 0
question28 = 0
question29 = 0
question30 = 0
question31 = 0
question32 = 0
question33 = 0
question34 = 0
question35 = 0
question36 = 0
question37 = 0
question38 = 0
question39 = 0
question40 = 0
question41 = 0
question42 = 0
question43 = 0
question44 = 0
question45 = 0
question46 = 0
question47 = 0
question48 = 0
question49 = 0
question50 = 0
question51 = 0
question52 = 0
question53 = 0
question54 = 0
question55 = 0
question56 = 0
question57 = 0
question58 = 0
question59 = 0
question60 = 0
question61 = 0
question62 = 0
question63 = 0
question64 = 0








for a in range(1,11):
    if game == "+":
        while question in range(10):
            print()
            question = question + 1
            number = random.randint(0,20)
            number1 = random.randint(0,50)
            answer = (number+number1)
            print(question,".)",number,"plus",number1)
            total_a = float(input("What is the answer?"))
            if total_a == answer:                                                                      #For when you start the game by answering addition questions.
                print("Correct")
                mark = mark + 1
            else:
                print("INCORRECT. The right answer is", answer)
                break

    if game == "-":
        while question16 in range(10):
            print()
            question16 = question16 + 1
            number32 = random.randint(10,50)
            number33 = random.randint(0,30)
            answer16 = (number32-number33)                                                          #For when you start the game by answering subtraction questions.
            print(question16,".)",number32,"minus",number33)
            total_q = float(input("What is the answer?"))
            if total_q == answer16:
                print("Correct")
                mark = mark + 1
            else:
                print("INCORRECT. The right answer is", answer16)
                break

    if game == "*":
        while question32 in range(10):
            print()
            question32 = question32 + 1
            number64 = random.randint(0,20)
            number65 = random.randint(0,20)
            answer32 = (number64*number65)                                                          #For when you start the game by answering mutliplication questions.
            print(question32,".)",number64,"times",number65)
            total_af = float(input("What is the answer?"))
            if total_af == answer32:
                print("Correct")
                mark = mark + 1
            else:
                print("INCORRECT. The right answer is", answer32)
                break

    if game == "/":
        while question48 in range(10):
            print()
            question48 = question48 + 1
            number96 = random.randint(15,60)
            number97 = random.randint(1,15)
            answer48 = round(number96/number97,2)                                                   #For when you start the game by answering division questions.
            print(question48,".)",number96,"divided by",number97)
            total_av = float(input("What is the answer?"))
            if total_av == answer48:
                print("Correct")
                mark = mark + 1
            else:
                print("INCORRECT. The right answer is", answer48)
                break
            
    


            

if question == (10):
    print()
    game1 = input("Would you like to do subtraction(-), multiplication(*) or division(/)?")      #After you asnwer ten addition questions, you will be asked
                                                                                                 #what operation you want to try out of the three left. 
    for b in range(1,11):
        if game1 == "-":
            while question1 in range(10):
                print()
                question1 = question1 + 1
                number2 = random.randint(10,50)
                number3 = random.randint(0,30)                                                  #Code for when you try out subtraction after doing addition
                answer1 = (number2-number3)                                                     #in the the first round.
                print(question1,".)",number2,"minus",number3)
                total_b = float(input("What is the answer?"))
                if total_b == answer1:
                    print("Correct")
                    mark1 = mark1 + 1
                else:
                    print("INCORRECT. The right answer is", answer1)
                    break

            if question1 == (10):
                print()
                game2 = input("Would you like to do multiplication(*) or division(/)?")           #Once you finish subtraction in the second round,
                                                                                                  #you will be asked in the third if you want to try
                                                                                                  #multiplication or division
                for c in range(1,11):
                    if game2 == "*":
                        while question2 in range(10):
                            print()
                            question2 = question2 + 1
                            number4 = random.randint(0,20)
                            number5 = random.randint(0,20)
                            answer2 = (number4*number5)
                            print(question2,".)",number4,"times",number5)                          #If you choose to do multiplication in the third round.
                            total_c = float(input("What is the answer?"))
                            if total_c == answer2:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer2)
                                break

                        if question2 == (10):
                            print()
                            game3 = print("You must complete division questions. Enjoy!")         #After doing multiplication in the third round, you must
                                                                                                  #do division in the fourth round.
                            for d in range(1,11):
                                while question3 in range(10):
                                    print()
                                    question3 = question3 + 1
                                    number6 = random.randint(15,60)
                                    number7 = random.randint(1,15)
                                    answer3 = round(number6/number7,2)
                                    print(question3,".)",number6,"divided",number7)
                                    total_d = float(input("What is the answer?"))
                                    if total_d == answer3:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer3)
                                        break

                                if question3 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test") #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                

                    elif game2 == "/":
                        while question4 in range(10):
                            print()
                            question4 = question4 + 1
                            number8 = random.randint(15,60)
                            number9 = random.randint(1,15)
                            answer4 = round(number8/number9,2)
                            print(question4,".)",number8,"divided by",number9)                             #If you choose to do division in the third round after
                            total_e = float(input("What is the answer?"))                                  #doing addition in the first round and subtraction in the
                            if total_e == answer4:                                                         #second.
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer4)
                                break

                        if question4 == (10):
                            print()
                            game4 = print("You must complete multiplication questions. Enjoy!")             #You must complete multiplication questions in the fourth
                                                                                                            #round after having division in the third.
                            for e in range(1,11):
                                while question5 in range(10):
                                    print()
                                    question5 = question5 + 1
                                    number10 = random.randint(0,20)
                                    number11 = random.randint(0,20)
                                    answer5 = (number10*number11)
                                    print(question5,".)",number10,"times",number11)
                                    total_f = float(input("What is the answer?"))
                                    if total_f == answer5:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer5)
                                    break

                                if question5 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")    #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break

                                      
                

            
        elif game1 == "*":                                                                                     #If you choose to do multiplication in the second round
            while question6 in range(10):                                                                      #after doing addition in the first.
                print()
                question6 = question6 + 1
                number12 = random.randint(0,20)
                number13 = random.randint(0,20)
                answer6 = (number12*number13)
                print(question6,".)",number12,"times",number13)
                total_g = float(input("What is the answer?"))
                if total_g == answer6:
                    print("Correct")
                    mark1 = mark1 + 1
                else:
                    print("INCORRECT. The right answer is", answer6)
                    break


            if question6 == (10):
                print()
                game5 = input("Would you like to do subtraction(-) or division(/)?")                           #You will be asked which two operations you would like
                                                                                                               #to try; either subtraction or division after doing 
                for f in range(1,11):                                                                          #addition in the first round and multiplication in the 
                    if game5 == "-":                                                                           #second round.
                        while question7 in range(10):
                            print()
                            question7 = question7 + 1
                            number14 = random.randint(10,50)
                            number15 = random.randint(0,30)
                            answer7 = (number14-number15)
                            print(question7,".)",number14,"minus",number15)                                   #If you choose to try subtraction in the third round.
                            total_h = float(input("What is the answer?"))
                            if total_h == answer7:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer7)
                                break

                        if question7 == (10):
                            print()
                            game6 = print("You must do division questions now. Enjoy")                      #You must do division questions in the fourth round if you
                                                                                                            #do subtraction in the third round. 
                            for g in range(1,11):
                                while question8 in range(10):
                                    print()
                                    question8= question8 + 1
                                    number16 = random.randint(15,60)
                                    number17 = random.randint(1,15)
                                    answer8 = round(number16/number17,2)
                                    print(question8,".)",number16,"divided by",number17)
                                    total_i = float(input("What is the answer?"))
                                    if total_i == answer8:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer8)
                                        break

                                if question8 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")      #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                    
                            
  
                    elif game5 == "/":                                                                          #If you choose to do division in the third round.
                        while question9 in range(10):
                            print()
                            question9 = question9 + 1
                            number18 = random.randint(15,60)
                            number19 = random.randint(1,15)
                            answer9 = round(number18/number19,2)
                            print(question9,".)",number18,"divided by",number19)
                            total_j = float(input("What is the answer?"))
                            if total_j == answer9:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer9)
                                break

                        if question9 == (10):
                            print()
                            game7 = print("You must do subtraction questions now. Enjoy")                        #You must do subtraction in the fourth round if you 
                                                                                                                 #do division in the third round.
                            for h in range(1,11):
                                while question10 in range(10):
                                    print()
                                    question10= question10 + 1
                                    number20 = random.randint(10,50)
                                    number21 = random.randint(0,30)
                                    answer10 = (number20-number21)
                                    print(question10,".)",number20,"minus",number21)
                                    total_k = float(input("What is the answer?"))
                                    if total_k == answer10:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer10)
                                        break

                                if question10 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")         #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                

                    

                
                


        elif game1 == "/":                                                              #If you choose to do division after doing addition in the first round. 
            while question11 in range(10):
                print()
                question11 = question11 + 1
                number22 = random.randint(15,50)
                number23 = random.randint(1,15)
                answer11 = round(number22/number23,2)
                print(question11,".)",number22,"divided by",number23)
                total_l = float(input("What is the answer?"))
                if total_l == answer11:
                    print("Correct")
                    mark1 = mark1 + 1
                else:
                    print("INCORRECT. The right answer is", answer11)
                    break

            if question11 == (10):
                print()
                game8 = input("Would you like to do subtraction(-) or multiplication(*)?")         #You will be asked which operation you would like to do after
                                                                                                   #doing addition in the first round and division in the second 
                for i in range(1,11):                                                              #round. The operations available to try are subtraction and 
                    if game8 == "-":                                                               #multiplication.
                        while question12 in range(10):
                            print()
                            question12 = question12 + 1
                            number24 = random.randint(10,50)
                            number25 = random.randint(0,30)
                            answer12 = (number24-number25)
                            print(question12,".)",number24,"minus",number25)                       #If you choose to do subtraction in the third round after division.
                            total_m = float(input("What is the answer?"))
                            if total_m == answer12:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer12)
                                break

                        if question12 == (10):
                            print()
                            game9 = print("You must complete multiplication questions. Enjoy")  #You must do multiplication after doing subtraction in the third round.

                            for j in range(1,11):
                                while question13 in range(10):
                                    print()
                                    question13= question13 + 1
                                    number26 = random.randint(0,20)
                                    number27 = random.randint(0,20)
                                    answer13 = (number26*number27)
                                    print(question13,".)",number26,"times",number27)
                                    total_n = float(input("What is the answer?"))
                                    if total_n == answer13:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer13)
                                        break

                                if question13 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")    #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                            

                    if game8 == "*":
                        while question14 in range(10):                                                     #If you choose to do multiplication in the third round
                            print()                                                                        #instead of doing subtraction.
                            question14 = question14 + 1
                            number28 = random.randint(0,20)
                            number29 = random.randint(0,20)
                            answer14 = (number28*number29)
                            print(question14,".)",number28,"times",number29)
                            total_o = float(input("What is the answer?"))
                            if total_o == answer14:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer14)
                                break


                        if question14 == (10):
                            print()
                            game10 = print("You must complete subtraction questions. Enjoy")             #You must do subtraction in the fourth round.

                            for k in range(1,11):
                                while question15 in range(10):
                                    print()
                                    question15= question15 + 1
                                    number30 = random.randint(10,50)
                                    number31 = random.randint(0,30)
                                    answer15 = (number30-number31)
                                    print(question15,".)",number30,"minus",number31)
                                    total_p = float(input("What is the answer?"))
                                    if total_p == answer15:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer15)
                                        break

                                if question15 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")           #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break

  
                    
if question16 == (10):
    print()
    game11 = input("Would you like to do addition(+), multiplication(*) or division(/)?")                   #If you choose to do subtraction in the first round         
                                                                                                            #you will be asked what operations you want to try next                                                                                           
    for l in range(1,11):                                                                                   #from the following three operations left.
        if game11 == "+":
            while question17 in range(10):
                print()
                question17 = question17 + 1
                number34 = random.randint(0,50)                                                             #If you choose to do addition in the second round.
                number35 = random.randint(0,50)
                answer17 = (number34+number35)
                print(question17,".)",number34,"plus",number35)
                total_q = float(input("What is the answer?"))
                if total_q == answer17:
                    print("Correct")
                    mark1 = mark1 + 1
                else:
                    print("INCORRECT. The right answer is", answer17)
                    break

            if question17 == (10):
                print()
                game12 = input("Would you like to do multiplication(*) or division(/)?")            #You will be asked if you want to try multiplication or division
                                                                                                    #after doing subtraction in the first round and additon in the
                for m in range(1,11):                                                               #second round.
                    if game12 == "*":
                        while question18 in range(10):
                            print()
                            question18 = question18 + 1
                            number36 = random.randint(0,20)
                            number37 = random.randint(0,20)
                            answer18 = (number36*number37)
                            print(question18,".)",number36,"times",number37)                        #If you choose to do multiplication in the third round.
                            total_r = float(input("What is the answer?"))
                            if total_r == answer18:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer18)
                                break

                        if question18 == (10):
                            print()
                            game13 = print("You must complete division questions. Enjoy!")      #Then you must do division in the fourth round.

                            for n in range(1,11):
                                while question19 in range(10):
                                    print()
                                    question19 = question19 + 1
                                    number38 = random.randint(15,50)
                                    number39 = random.randint(1,15)
                                    answer19 = round(number38/number39,2)
                                    print(question19,".)",number38,"divided",number39)
                                    total_s = float(input("What is the answer?"))
                                    if total_s == answer19:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer19)
                                        break

                                if question19 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")   #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                
                                

                    elif game12 == "/":                                                                         #If you choose to do division in the third round.
                        while question20 in range(10):
                            print()
                            question20 = question20 + 1
                            number40 = random.randint(15,50)
                            number41 = random.randint(1,15)
                            answer20 = round(number40/number41,2)
                            print(question20,".)",number40,"divided by",number41)
                            total_t = float(input("What is the answer?"))
                            if total_t == answer20:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer20)
                                break

                        if question20 == (10):
                            print()
                            game14 = print("You must complete multiplication questions. Enjoy!")            #Then you must do multiplication in the fourth round.

                            for o in range(1,11):
                                while question21 in range(10):
                                    print()
                                    question21 = question21 + 1
                                    number42 = random.randint(0,20)
                                    number43 = random.randint(0,20)
                                    answer21 = (number42*number43)
                                    print(question21,".)",number42,"times",number43)
                                    total_u = float(input("What is the answer?"))
                                    if total_u == answer21:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer21)
                                    break

                                if question21 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")    #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break

                                      
                

            
        elif game11 == "*":
            while question22 in range(10):                                                  #If you choose to do multiplication in the second round after doing 
                print()                                                                     #subtraction in the first round.
                question22 = question22 + 1                                             
                number44 = random.randint(0,20)
                number45 = random.randint(0,20)
                answer22 = (number44*number45)
                print(question22,".)",number44,"times",number45)
                total_v = float(input("What is the answer?"))
                if total_v == answer22:
                    print("Correct")
                    mark1 = mark1 + 1
                else:
                    print("INCORRECT. The right answer is", answer22)
                    break


            if question22 == (10):
                print()
                game15 = input("Would you like to do addition(+) or division(/)?")       #You will be asked if you want to try addition or division in the
                                                                                         #third round.
                for p in range(1,11):
                    if game15 == "+":
                        while question23 in range(10):
                            print()
                            question23 = question23 + 1
                            number46 = random.randint(0,20)
                            number47 = random.randint(0,50)
                            answer23 = (number46+number47)
                            print(question23,".)",number46,"plus",number47)           #If you choose to do addition in the third round.
                            total_w = float(input("What is the answer?"))
                            if total_w == answer23:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer23)
                                break

                        if question23 == (10):
                            print()
                            game16 = print("You must do division questions now. Enjoy")  #Then you must do division in the fourth round.

                            for q in range(1,11):
                                while question24 in range(10):
                                    print()
                                    question24= question24 + 1
                                    number48 = random.randint(15,50)
                                    number49 = random.randint(1,15)
                                    answer24 = round(number48/number49,2)
                                    print(question24,".)",number48,"divided by",number49)
                                    total_x = float(input("What is the answer?"))
                                    if total_x == answer24:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer24)
                                        break

                                if question24 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")       #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                
                                        
                                    
                            

                    elif game15 == "/":
                        while question25 in range(10):
                            print()
                            question25 = question25 + 1
                            number50 = random.randint(15,50)
                            number51 = random.randint(1,15)
                            answer25 = round(number50/number51,2)
                            print(question25,".)",number50,"divided by",number51)               #If you choose to do division in the third round.
                            total_y = float(input("What is the answer?"))
                            if total_y == answer25:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer25)
                                break

                        if question25 == (10):
                            print()
                            game17 = print("You must do addition questions now. Enjoy")       #Then you must do addition in the fourth round.

                            for r in range(1,11):
                                while question26 in range(10):
                                    print()
                                    question26 = question26 + 1
                                    number52 = random.randint(0,20)
                                    number53 = random.randint(0,50)
                                    answer26 = (number52+number53)
                                    print(question26,".)",number52,"plus",number53)
                                    total_z = float(input("What is the answer?"))
                                    if total_z == answer26:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer26)
                                        break

                                if question26 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")    #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                    
                                

                    

                
                


        elif game11 == "/":                                                                  #If you choose to do division in the second round after
            while question27 in range(10):                                                   #doing subtraction in the first round.
                print()                                                             
                question27 = question27 + 1
                number54 = random.randint(15,50)
                number55 = random.randint(1,15)
                answer27 = round(number54/number55,2)
                print(question27,".)",number54,"divided by",number55)
                total_aa = float(input("What is the answer?"))
                if total_aa == answer27:
                    print("Correct")
                    mark1 = mark1 + 1
                else:
                    print("INCORRECT. The right answer is", answer27)
                    break

            if question27 == (10):
                print()
                game18 = input("Would you like to do addition(+) or multiplication(*)?")   #Then you will be asked if you want to try addition or multiplication 
                                                                                           #in the third round after doing subtraction and division previously. 
                for s in range(1,11):
                    if game18 == "+":
                        while question28 in range(10):
                            print()
                            question28 = question28 + 1
                            number56 = random.randint(0,20)
                            number57 = random.randint(0,50)
                            answer28 = (number56+number57)
                            print(question28,".)",number56,"plus",number57)                 #If you choose to do addition in the third round. 
                            total_ab = float(input("What is the answer?"))
                            if total_ab == answer28:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer28)
                                break

                        if question28 == (10):
                            print()
                            game19 = print("You must complete multiplication questions. Enjoy")     #Then you must do multiplication in the fourth round.  

                            for t in range(1,11):
                                while question29 in range(10):
                                    print()
                                    question29= question29 + 1
                                    number58 = random.randint(0,20)
                                    number59 = random.randint(0,20)
                                    answer29 = (number58*number59)
                                    print(question29,".)",number58,"times",number59)
                                    total_ac = float(input("What is the answer?"))
                                    if total_ac == answer29:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer29)
                                        break

                                if question29 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")         #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                    
                            

                    if game18 == "*":                                                           #If you choose to do multiplication in the third round
                        while question30 in range(10):                                          #instead of doing addition.
                            print()
                            question30 = question30 + 1
                            number60 = random.randint(0,20)
                            number61 = random.randint(0,20)
                            answer30 = (number60*number61)
                            print(question30,".)",number60,"times",number61)
                            total_ad = float(input("What is the answer?"))
                            if total_ad == answer30:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer30)
                                break


                        if question30 == (10):
                            print()
                            game20 = print("You must complete addition questions. Enjoy")        #Then you must do addition in the fourth round. 

                            for u in range(1,11):
                                while question31 in range(10):
                                    print()
                                    question31 = question31 + 1
                                    number62 = random.randint(0,20)
                                    number63 = random.randint(0,50)
                                    answer31 = (number62+number63)
                                    print(question31,".)",number62,"plus",number63)
                                    total_ae = float(input("What is the answer?"))
                                    if total_ae == answer31:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer31)
                                        break

                                if question31 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")             #Total sum of your marks of forty.
     
                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                






if question32 == (10):
    print()
    game21 = input("Would you like to do addition(+), subtraction(-), or division(/)?")                 #Starting of multiplication.
    

    for v in range(1,11):
        if game21 == "+":
            while question33 in range(10):                                      #If you choose to do addition in the second round.
                print()
                question33 = question33 + 1
                number66 = random.randint(0,20)
                number67 = random.randint(0,50)
                answer33 = (number66+number67)
                print(question33,".)",number66,"plus",number67)
                total_ag = float(input("What is the answer?"))
                if total_ag == answer33:
                    print("Correct")
                    mark1 = mark1 + 1
                else:
                    print("INCORRECT. The right answer is", answer33)
                    break

            if question33 == (10):
                print()
                game22 = input("Would you like to do subtraction(-) or division(/)?")          #You will be asked if you want to try subtraction or division in the
                                                                                               #third round.
                for w in range(1,11):
                    if game22 == "-":
                        while question34 in range(10):
                            print()
                            question34 = question34 + 1
                            number68 = random.randint(10,50)
                            number69 = random.randint(0,30)
                            answer34 = (number68-number69)
                            print(question34,".)",number68,"minus",number69)                            #If you want to try subtraction in the third round
                            total_ah = float(input("What is the answer?"))
                            if total_ah == answer34:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer34)
                                break

                        if question34 == (10):
                            print()
                            game23 = print("You must complete division questions. Enjoy!")                  #Then you must do division in the fourth round.

                            for x in range(1,11):                                                   
                                while question35 in range(10):
                                    print()
                                    question35 = question35 + 1
                                    number70 = random.randint(15,50)
                                    number71 = random.randint(1,15)
                                    answer35 = round(number70/number71,2)
                                    print(question35,".)",number70,"divided",number71)
                                    total_ai = float(input("What is the answer?"))
                                    if total_ai == answer35:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer35)
                                        break

                                if question35 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")        #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                    
                                
                                

                    elif game22 == "/":                                                                     #If you choose to do division in the third round instead
                        while question36 in range(10):                                                      #of doing subtraction.
                            print()
                            question36 = question36 + 1
                            number72 = random.randint(15,50)
                            number73 = random.randint(1,15)
                            answer36 = round(number72/number73,2)
                            print(question36,".)",number72,"divided by",number73)
                            total_aj = float(input("What is the answer?"))
                            if total_aj == answer36:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer36)
                                break

                        if question36 == (10):
                            print()
                            game24 = print("You must complete subtraction questions. Enjoy!")               #Then you must do subtraction in the fourth round.

                            for y in range(1,11):       
                                while question37 in range(10):
                                    print()
                                    question37 = question37 + 1
                                    number74 = random.randint(10,50)
                                    number75 = random.randint(0,30)
                                    answer37 = (number74-number75)
                                    print(question37,".)",number74,"minus",number75)
                                    total_ak = float(input("What is the answer?"))
                                    if total_ak == answer37:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer37)
                                    break

                                if question37 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")          #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                    

                                      
                

            
        elif game21 == "-":                                                                     #If you choose to do subtraction in the second round.
            while question38 in range(10):
                print()
                question38 = question38 + 1
                number76 = random.randint(10,50)
                number77 = random.randint(0,30)
                answer38 = (number76-number77)
                print(question38,".)",number76,"minus",number77)
                total_al = float(input("What is the answer?"))
                if total_al == answer38:
                    print("Correct")
                    mark1 = mark1 + 1
                else:
                    print("INCORRECT. The right answer is", answer38)
                    break


            if question38 == (10):
                print()
                game25 = input("Would you like to do addition(+) or division(/)?")                      #You will get the option to do either addition or division
                                                                                                        #in the third round.
                for z in range(1,11):
                    if game25 == "+":
                        while question39 in range(10):
                            print()
                            question39 = question39 + 1
                            number78 = random.randint(0,20)
                            number79 = random.randint(0,50)
                            answer39 = (number78+number79)
                            print(question39,".)",number78,"plus",number79)                         #If you choose addition in the third round.
                            total_am = float(input("What is the answer?"))
                            if total_am == answer39:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer39)
                                break

                        if question39 == (10):
                            print()
                            game26 = print("You must do division questions now. Enjoy")             #Then you must do division in the fourth round.

                            for aa in range(1,11):
                                while question40 in range(10):
                                    print()
                                    question40= question40 + 1
                                    number80 = random.randint(15,50)
                                    number81 = random.randint(1,15)
                                    answer40 = round(number80/number81,2)
                                    print(question40,".)",number80,"divided by",number81)
                                    total_an = float(input("What is the answer?"))
                                    if total_an == answer40:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer40)
                                        break

                                if question40 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")      #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                    
                                    
                            

                    elif game25 == "/":                                                         #If you choose to do division in the third round.
                        while question41 in range(10):
                            print()
                            question41 = question41 + 1
                            number82 = random.randint(15,50)
                            number83 = random.randint(1,15)
                            answer41 = round(number82/number83,2)
                            print(question41,".)",number82,"divided by",number83)
                            total_ao = float(input("What is the answer?"))
                            if total_ao == answer41:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer41)
                                break

                        if question41 == (10):
                            print()
                            game27 = print("You must do addition questions now. Enjoy")                             #Then you must do addition in the fourth round.

                            for ab in range(1,11):
                                while question42 in range(10):
                                    print()
                                    question42 = question42 + 1
                                    number84 = random.randint(0,20)
                                    number85 = random.randint(0,50)
                                    answer42 = (number84+number85)
                                    print(question42,".)",number84,"plus",number85)
                                    total_ap = float(input("What is the answer?"))
                                    if total_ap == answer42:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer42)
                                        break

                                if question42 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")           #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                    
                                

                    

                
                


        elif game21 == "/":                                                                 #If you choose to do division in the second round.
            while question43 in range(10):
                print()
                question43 = question43 + 1
                number86 = random.randint(15,50)
                number87 = random.randint(1,15)
                answer43 = round(number86/number87,2)
                print(question43,".)",number86,"divided by",number87)
                total_aq = float(input("What is the answer?"))
                if total_aq == answer43:
                    print("Correct")
                    mark1 = mark1 + 1
                else:
                    print("INCORRECT. The right answer is", answer43)
                    break

            if question43 == (10):
                print()
                game28 = input("Would you like to do addition(+) or subtraction(-)?")           #You will be asked if you want to try addition or subtraction in the 
                                                                                                #third round.
                for ac in range(1,11):
                    if game28 == "+":
                        while question44 in range(10):
                            print()
                            question44 = question44 + 1
                            number88 = random.randint(0,20)
                            number89 = random.randint(0,50)                                         #If you choose to do addition in the third round. 
                            answer44 = (number88+number89)
                            print(question44,".)",number88,"plus",number89)
                            total_ar = float(input("What is the answer?"))
                            if total_ar == answer44:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer44)
                                break

                        if question44 == (10):
                            print()
                            game29 = print("You must complete subtraction questions. Enjoy")            #Then you must do subtraction in the fourth round.

                            for ad in range(1,11):
                                while question45 in range(10):
                                    print()
                                    question45= question45 + 1
                                    number90 = random.randint(10,50)
                                    number91 = random.randint(0,30)
                                    answer45 = (number90-number91)
                                    print(question45,".)",number90,"minus",number91)
                                    total_as = float(input("What is the answer?"))
                                    if total_as == answer45:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer45)
                                        break

                                if question45 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")              #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                    
                            

                    if game28 == "-":                                                                       #If you choose to do subtraction in the third round.
                        while question46 in range(10):
                            print()
                            question46 = question46 + 1
                            number92 = random.randint(10,50)
                            number93 = random.randint(0,30)
                            answer46 = (number92-number93)
                            print(question46,".)",number92,"minus",number93)
                            total_at = float(input("What is the answer?"))
                            if total_at == answer46:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer46)
                                break


                        if question46 == (10):
                            print()
                            game30 = print("You must complete addition questions. Enjoy")               #Then you will be asked to do addition in the fourth round.

                            for ae in range(1,11):
                                while question47 in range(10):
                                    print()
                                    question47 = question47 + 1
                                    number94 = random.randint(0,20)
                                    number95 = random.randint(0,50)
                                    answer47 = (number94+number95)
                                    print(question47,".)",number94,"plus",number95)
                                    total_au = float(input("What is the answer?"))
                                    if total_au == answer47:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer47)
                                        break

                                if question47 == (10):
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")      #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                


if question48 == (10):
    print()
    game31 = input("Would you like to do addition(+), subtraction(-), or multiplication(*)?")                       #Starting of division.
    

    for af in range(1,11):
        if game31 == "+":
            while question49 in range(10):                                                      #If you choose to do addition in the second round.
                print()
                question49 = question49 + 1
                number98 = random.randint(0,50)
                number99 = random.randint(0,50)
                answer49 = (number98+number99)
                print(question49,".)",number98,"plus",number99)
                total_aw = float(input("What is the answer?"))
                if total_aw == answer49:
                    print("Correct")
                    mark1 = mark1 + 1
                else:
                    print("INCORRECT. The right answer is", answer49)
                    break

            if question49 == (10):
                print()
                game32 = input("Would you like to do subtraction(-) or multiplication(*)?")     #You will be asked if you want to try subtraction or multiplication
                                                                                                #in the third round.
                for ag in range(1,11):
                    if game32 == "-":
                        while question50 in range(10):
                            print()
                            question50 = question50 + 1
                            number100 = random.randint(10,50)
                            number101 = random.randint(0,30)                                        #If you choose to do subtraction in the third round.
                            answer50 = (number100-number101)
                            print(question50,".)",number100,"minus",number101)
                            total_ax = float(input("What is the answer?"))
                            if total_ax == answer50:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer50)
                                break

                        if question50 == (10):
                            print()
                            game33 = print("You must complete multiplication questions. Enjoy!")            #Then you must do multiplcation in the fourth round.

                            for ah in range(1,11):                                                   
                                while question51 in range(10):
                                    print()
                                    question51 = question51 + 1
                                    number102 = random.randint(0,20)
                                    number103 = random.randint(0,20)
                                    answer51 = (number102*number103)
                                    print(question51,".)",number102,"times",number103)
                                    total_ay = float(input("What is the answer?"))
                                    if total_ay == answer51:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer51)
                                        break

                                if question51 == (10):
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")              #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                    
                                
                                

                    elif game32 == "*":                                                             #If you choose to do multiplication in the third round.
                        while question52 in range(10):
                            print()
                            question52 = question52 + 1
                            number104 = random.randint(0,20)
                            number105 = random.randint(0,20)
                            answer52 = (number104*number105)
                            print(question52,".)",number104,"times",number105)
                            total_az = float(input("What is the answer?"))
                            if total_az == answer52:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer52)
                                break

                        if question52 == (10):
                            print()
                            game34 = print("You must complete subtraction questions. Enjoy!")           #Then you must do subtraction in the fourth round.

                            for ai in range(1,11):       
                                while question53 in range(10):
                                    print()
                                    question53 = question53 + 1
                                    number106 = random.randint(10,50)
                                    number107 = random.randint(0,30)
                                    answer53 = (number106-number107)
                                    print(question53,".)",number106,"minus",number107)
                                    total_ba = float(input("What is the answer?"))
                                    if total_ba == answer53:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer53)
                                    break

                                if question53 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")          #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                    

                                      
                

            
        elif game31 == "-":                                                             #If you choose subtraction in the second round instead of addition.
            while question54 in range(10):
                print()
                question54 = question54+ 1
                number108 = random.randint(10,50)
                number109 = random.randint(0,30)
                answer54 = (number108-number109)
                print(question54,".)",number108,"minus",number109)
                total_bb = float(input("What is the answer?"))
                if total_bb == answer54:
                    print("Correct")
                    mark1 = mark1 + 1
                else:
                    print("INCORRECT. The right answer is", answer54)
                    break


            if question54 == (10):
                print()
                game35 = input("Would you like to do addition(+) or multiplication(*)?")  #You will be asked if you want to try addition or multiplcation in the 
                                                                                          #third round.
                for aj in range(1,11):
                    if game35 == "+":
                        while question55 in range(10):
                            print()
                            question55 = question55 + 1
                            number110 = random.randint(0,20)
                            number111 = random.randint(0,50)                                #If you choose to try addition in the third round.
                            answer55 = (number110+number111)
                            print(question55,".)",number110,"plus",number111)
                            total_bc = float(input("What is the answer?"))
                            if total_bc == answer55:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer55)
                                break

                        if question55 == (10):
                            print()
                            game36 = print("You must do multiplication questions now. Enjoy")           #Then you must do multiplciation questions in the fourth round.

                            for ak in range(1,11):
                                while question56 in range(10):
                                    print()
                                    question56= question56 + 1
                                    number112 = random.randint(0,20)
                                    number113 = random.randint(0,20)
                                    answer56 =(number112*number113)
                                    print(question56,".)",number112,"times",number113)
                                    total_bd = float(input("What is the answer?"))
                                    if total_bd == answer56:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer56)
                                        break

                                if question56 == (10):
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")          #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                    
                                    
                            

                    elif game35 == "*":                                         #If you choose to do multiplication in third round. 
                        while question57 in range(10):
                            print()
                            question57 = question57 + 1
                            number114 = random.randint(1,20)
                            number115 = random.randint(1,20)
                            answer57 = (number114*number115)
                            print(question57,".)",number114,"times",number115)
                            total_be = float(input("What is the answer?"))
                            if total_be == answer57:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer57)
                                break

                        if question57 == (10):
                            print()
                            game37 = print("You must do addition questions now. Enjoy")         #Then you must try addition in the fourth round.

                            for al in range(1,11):
                                while question58 in range(10):
                                    print()
                                    question58 = question58 + 1
                                    number116 = random.randint(0,20)
                                    number117 = random.randint(0,50)
                                    answer58 = (number116+number117)
                                    print(question58,".)",number116,"plus",number117)
                                    total_bf = float(input("What is the answer?"))
                                    if total_bf == answer58:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer58)
                                        break

                                if question58 == (10):
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")          #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                    
                                

                    

                
                


        elif game31 == "*":                                                             #If you choose to do multiplication in the second round.
            while question59 in range(10):
                print()
                question59 = question59 + 1
                number118 = random.randint(1,20)
                number119 = random.randint(1,20)
                answer59 = (number118*number119)
                print(question59,".)",number118,"times",number119)
                total_bg = float(input("What is the answer?"))
                if total_bg == answer59:
                    print("Correct")
                    mark1 = mark1 + 1
                else:
                    print("INCORRECT. The right answer is", answer59)
                    break

            if question59 == (10):
                print()
                game38 = input("Would you like to do addition(+) or subtraction(-)?")           #You will be asked if you want to try addition or subtraction in the
                                                                                                #third round.
                for am in range(1,11):
                    if game38 == "+":
                        while question60 in range(10):
                            print()
                            question60 = question60 + 1
                            number120 = random.randint(0,20)
                            number121 = random.randint(0,50)
                            answer60 = (number120+number121)                                        #If you choose to do addition in the third round.
                            print(question60,".)",number120,"plus",number121)
                            total_bh = float(input("What is the answer?"))
                            if total_bh == answer60:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer60)
                                break

                        if question60 == (10):
                            print()
                            game39 = print("You must complete subtraction questions. Enjoy")                #Then you must do subtraction in the fourth round.

                            for an in range(1,11):
                                while question61 in range(10):
                                    print()
                                    question61= question61 + 1
                                    number122 = random.randint(10,50)
                                    number123 = random.randint(0,30)
                                    answer61 = (number122-number123)
                                    print(question61,".)",number122,"minus",number123)
                                    total_bi = float(input("What is the answer?"))
                                    if total_bi == answer61:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer61)
                                        break

                                if question61 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")      #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                    
                            

                    if game38 == "-":
                        while question62 in range(10):                                                  #If you choose to do subtraction in the third round.
                            print()
                            question62 = question62 + 1
                            number124 = random.randint(10,50)
                            number125 = random.randint(0,30)
                            answer62 = (number124-number125)
                            print(question62,".)",number124,"minus",number125)
                            total_bk = float(input("What is the answer?"))
                            if total_bk == answer62:
                                print("Correct")
                                mark2 = mark2 + 1
                            else:
                                print("INCORRECT. The right answer is", answer62)
                                break


                        if question62 == (10):
                            print()
                            game40 = print("You must complete addition questions. Enjoy")           #Then you must do addition in the fourth round.

                            for ao in range(1,11):
                                while question63 in range(10):
                                    print()
                                    question63 = question63 + 1
                                    number126 = random.randint(0,20)
                                    number127 = random.randint(0,50)
                                    answer63 = (number126+number127)
                                    print(question63,".)",number126,"plus",number127)
                                    total_bl = float(input("What is the answer?"))
                                    if total_bl == answer63:
                                        print("Correct")
                                        mark3 = mark3 + 1
                                    else:
                                        print("INCORRECT. The right answer is", answer63)
                                        break

                                if question63 == (10):
                                    print()
                                    sum =(mark+mark1+mark2+mark3)
                                    print("You've gotten", sum,"out of the total forty marks on the test")          #Total sum of your marks of forty.

                                    if sum == (40):
                                        print("WOW, you did an amazing job! You've aced the game.")
                                    else:
                                        print("You can do better than that! Play again.")
                                    break
                                    

























   
