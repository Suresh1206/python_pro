import random
def guess(x):
    random_number = random.randint(1,x)
    guess_no = 0
    c = 3
    f = 0
    while c != 0:
        print(f"\nYou have {c} chance(s)")
        guess_no = int(input(f"Guess a number between 1 to {x} : "))
        if guess_no == random_number:
            print("\nYay......u WON!")
            f = 1
            break
        else:
            if c!=1:
                print("Oops!Try Again....")
            c -= 1
    if(f==0):
        print("You Lost!!!!!!")
        print("The number is : ",random_number)
    again = int(input("\nDo u want to play again 0(No) or 1(Yes) : "))
    if again == 0:
        print("\nThanks for playing!")
    else:
        print("\n Let's Start Again\n")
        c = 3
        (guess(x))
guess(9)