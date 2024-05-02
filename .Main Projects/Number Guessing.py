
                    
                    
            

        


print("Welcome to my Number guessing game !")
print("in this game , you have 5 attempts to guess the number which the coumputer guessed")
print("wish you good luck !")

import random as rn
Start_Command = input("Enter the start Command : ")
Attempts = 5
if Start_Command == "-o gc start" :
    
            for i in range(5) :
                
                user_input = int(input("Enter a number among 1 to 10 : "))
                Computer_guessing = rn.randint(1,10)
                if user_input != Computer_guessing :
                    Attempts = Attempts-1 
                    print("You got it wrong !")
                    print("The number you thought was ", user_input)
                    print("But the actual number was ", Computer_guessing)
                    print("You have", Attempts , "attempts left")
                    if Attempts == 0 :
                          print("No more attempts left !")
                         # =  print("You have", Attempts , "attempts left")

                    continue
                    
                else :
                    print("You got it")
                    break
                











