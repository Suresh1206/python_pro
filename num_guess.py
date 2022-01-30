import random
def guess(x):
    random_number = random.randint(1,x)
    guess_no = 0
    c = 3
    while c != 0:
        print(f"\nYou have {c} chance(s)")
        guess_no = int(input(f"Guess a number between 1 to {x} : "))
        c -= 1
        if guess_no != random_number and c != 0:
            print("Oops!Try Again....")
        else:
            if c == 0:
                print("\nChances r finished.")
            else:
                print("\nYay......u WON!")
                break
    again = int(input("\nDo u want to play again 0(No) or 1(Yes) : "))
    if again == 0:
        print("\nThanks for playing!")
    else:
        print("\n Let's Start Again\n")
        c = 3
        (guess(x))
guess(10)