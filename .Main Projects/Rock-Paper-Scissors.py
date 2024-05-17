import random as rn

options = ("rock","paper","scissors")
player = input("enter your move : ")
computer = rn.choice(options)

def play() :
    if player == "rock" and  computer == "scissors" :
        print("your move :", player)
        print("computer Move :", computer)
        print("Computer wins !!")
    if player == "rock" and  computer == "paper" :
        print("your move :", player)
        print("computer Move :", computer)
        print("Computer wins!!")
    if player == "rock" and  computer == "rock" :
        print("your move :", player)
        print("computer Move :", computer)
        print("It is a tie !!")

    if player == "paper" and  computer == "scissors" :
        print("your move :", player)
        print("computer Move :", computer)
        print("Computer wins !!")
    if player == "paper" and  computer == "paper" :
        print("computer Move :", computer)
        print("It is a tie !!")
    if player == "paper" and  computer == "rock" :
        print("your move :", player)
        print("computer Move :", computer)
        print("You win  !!")

    if player == "scissors" and  computer == "scissors" :
        print("your move :", player)
        print("computer Move :", computer)
        print("It is a tie !!")
    if player == "scissors" and  computer == "paper" :
        print("your move :", player)
        print("computer Move :", computer)
        print("You win !!")
    if player == "scissors" and  computer == "rock" :
        print("your move :", player)
        print("computer Move :", computer)
        print("Computer wins !!")

play ()
