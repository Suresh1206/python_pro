import random

def play():
    user = input("\nCHOOSE : r for rock,p for paper,s for scissor : ")
    computer = random.choice(["r","p","s"])
    if user == computer:
        print("\nTie..")
    elif is_win(user,computer):
        print("\nYOU WON!")
    else:
        print("\nYOU LOST!")

    inp = input("Do u want to play again..y or n : ")
    if inp == "y":
        play()
    else:
        print("\nThanks for playing....\n")
def is_win(user,computer):
    if (user=="r" and computer == "s") or (user=="p" and computer == "r") or (user=="s" and computer=="p"):
        return(True)
    
(play())

