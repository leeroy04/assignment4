from time import sleep
import random
import os

#code by Levi Vanberkel

def match():
    # Open the results file in append mode to track wins/losses
    with open('match_history.txt', 'a') as file:
        file.write("\n--- New Match ---\n")

        print("Ready?")
        sleep(2)
        print("3!")
        sleep(1)
        print("2!")
        sleep(1)
        print("1!")
        sleep(1)
        print("Go!")
        sleep(1)

        while True:
            print("Choose your weapon!")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            print("4. Surrender...")
            choice = int(input("Please Enter Your Choice: "))
            if choice == 1:
                weapon = 'Rock'
            elif choice == 2:
                weapon = 'Paper'
            elif choice == 3:
                weapon = 'Scissors'
            elif choice == 4:
                file.write("Surrendered :(")
                print("Too scared??")
                sleep(1)
                return False
            else:
                print("Incorrect Input, Please Try Again...")
                continue

            print(f"You chose {weapon}!")

            #calulcate the bot's weapon
            num = random.randint(1, 3)
            if num == 1:
                bot = 'Rock'
            elif num == 2:
                bot = 'Paper'
            elif num == 3:
                bot = 'Scissors'

           #determine the winner
            print("The bot is choosing...")
            sleep(1)
            print("...")
            sleep(1)
            print("...")
            sleep(1)
            print("Done!")
            sleep(1)
            print("The winner is...")
            sleep(3)

            if weapon == bot:
                print("It's a tie!")
                file.write(f"TIED---You had {weapon} and the bot had {bot}\n")
            elif (weapon == 'Rock' and bot == 'Scissors') or \
                 (weapon == 'Scissors' and bot == 'Paper') or \
                 (weapon == 'Paper' and bot == 'Rock'):
                result = 'You!'
                print(result)
                file.write(f"WON---You had {weapon} and the bot had {bot}\n")
            else:
                result = 'The bot!'
                print(result)
                file.write(f"LOST---You had {weapon} and the bot had {bot}\n")

            sleep(2)
            print(f"The bot had {bot}!")
            sleep(1)
            print("Returning to Menu...")
            sleep(2)
            break

def history():
    print("Printing Match History..")
    sleep(1)

    # Check if the file is empty or doesn't exist
    if not os.path.exists('match_history.txt') or os.path.getsize('match_history.txt') == 0:
        print("The match history file is empty or does not exist.")

    with open('match_history.txt', 'r') as file:
        for line in file:
            print(line, end='')
    print("")
    while True:
        userInput = int(input("Please enter '5' to return to Menu: "))
        if userInput == 5:
            break
        else:
            print("Incorrect Input..")

def clear():
    print("Clearing Match History..")
    with open('match_history.txt', 'w') as file:
        pass

    sleep(2)
    print("Done!")

def credit():
    print("Printing Credits...")
    sleep(2)
    print("Code by: Levi Vanberkel")
    sleep(2)
    print("Developed using PyCharm")
    sleep(2)
    print("No bots, rocks, papers, or scissors were harmed making this program")
    sleep(1)
    while True:
        userInput = int(input("Please enter '5' to return to Menu: "))
        if userInput == 5:
            break
        else:
            print("Incorrect Input..")


print("Welcome to Rock Paper Scissors!")
sleep(2)
print("Below you will find the menu, where you can play, quit, or view match history!")
sleep(2)
print("Good luck!")
sleep(2)

while True:
        print("1. New Match")
        print("2. View Match History")
        print("3. Clear Match History")
        print("4. Credits")
        print("5. Quit")
        userInput = int(input("Please Enter Your Choice: "))
        if userInput == 1:
            match()
        elif userInput == 2:
            history()
        elif userInput == 3:
            clear()
        elif userInput == 4:
            credit()
        elif userInput == 5:
            print("Quiting...")
            break
        else:
            print("Incorrect Input, Please Try Again...")
            continue

