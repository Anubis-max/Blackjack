import random
while True: 
    choice = input("Do you want to play a game? (y/n): ")

    if choice.lower() == "y":
        cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        player = 0
        computare = 0  

        while True:
            chances = 0
            i = 10

            print(f"Player: {player}\nComputare: {computare}")
            choice = input("Want to add a number? (y/n): ")
            
            if choice.lower() == "y":
                player += random.choice(cards)
            else:
                player += 0

            while i > 0:
                if computare + i <= 21:
                    chances += 1
                i -= 1
            if chances >= 5:
                computare += random.choice(cards)

            if player > 21:
                print("Player Busts! Computare wins!")
                break
            elif player == 21:
                print("Player wins!")
                break
            elif computare > 21:
                print("Computare Busts! Player wins!")
                break
            elif computare >= 17 and computare <= 21:
                if player > computare:
                    print("Player wins!")
                    break
                elif player == computare:
                    print("It's a tie!")
                    break
                else:
                    print("Computare wins!")
                    break
    else:
        print("Goodbye!")
    choice = str(input("Wanna play again? y/n : "))
    if choice == "y":
        pass
    else:
        print("Bye!")
        break