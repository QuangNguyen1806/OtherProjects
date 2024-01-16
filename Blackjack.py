import random

print("Welcome to Blackjack!")

Condition = True

while Condition:
    play = input("Would you like to play Blackjack? [y/n] ")
    if play == 'n':
        print("Thank you for playing!")
        Condition = False
    elif play == 'y':
        user_card1 = random.randint(1, 11)
        user_card2 = random.randint(1, 11)
        print("Your cards are worth", user_card1, "and", user_card2)

        user_score = user_card1 + user_card2
        user_wants_card = True
        while user_wants_card:
            choice = input("Would you like another card? [y/n] ")
            if choice == 'y':
                new_card = random.randint(1, 11)
                user_score += new_card
                print("Your score is now", user_score)
                if user_score > 21:
                    print("Bust! You went over 21. Your opponent wins!")
                    user_wants_card = False
            elif choice == 'n':
                user_wants_card = False
            else:
                print("Please enter 'y' for 'yes' or 'n' for 'no.")

        opponent_score = 0
        while opponent_score < 17:
            opponent_score += random.randint(1, 11)

        print("Your score is {}!".format(user_score))
        print("Your opponent's score is", opponent_score, "!")
        
        if user_score > 21:
            print("You went over 21. Your opponent wins!")
        elif opponent_score > 21:
            print("Your opponent went over 21. You win!")
        elif user_score == opponent_score:
            print("It's a draw!")
        elif user_score == 21:
            print("You win! Your score was 21.")
        elif opponent_score == 21:
            print("Your opponent wins! Their score was 21.")
        elif user_score > opponent_score:
            print("You win! Your score was higher.")
        else:
            print("Your opponent wins! Their score was higher.")
    else:
        print("Please enter 'y' for 'yes' or 'n' for 'no.")
