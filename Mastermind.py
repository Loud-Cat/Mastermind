import random

def create_comp_list(): # Create "computer" list, aka the secret code
    nums = [i+1 for i in range(7)]
    num_list = []
    
    for i in range(4):
        choice = random.choice(nums)
        while choice in num_list:
            choice = random.choice(nums)
        num_list.append(choice)
    
    return num_list

def get_guess(): # Get the user's guess, check for errors
    while True:
        num_issue = False
        unique_issue = False
        len_issue = False
        value_issue = False
        # defaults ^
        
        guess = input("Enter your guess (4 unique numbers between 1 and 7): ")
        for number in guess:
            try:
                if int(number) < 1 or int(number) > 7:
                    num_issue = True
            except ValueError:
                value_issue = True
        if (value_issue):
            # print("The guess format typically goes like this: abcd (not a b c d)")
            guess = guess.split()
            guess_text = ""
            for i in range(4):
                guess[i] = int(guess[i])
                guess_text += str(guess[i])
            # print("Don't worry. I've corrected it to " + str(guess_text))
        if num_issue:
            print("You can only use numbers 1-7 as guesses!")
        else:
            for number in guess:
                if guess.count(number) > 1:
                    unique_issue = True
            if unique_issue:
                print("You can only use each number once!")
            else:
                if len(guess) != 4:
                    len_issue = True
                if len_issue:
                    print("Your guess must consist of 4 numbers!")
                else:
                    guess_list = list(guess)
                    for i in range(4):
                        guess_list[i] = int(guess_list[i])
                    return guess_list

def check_values(comp, user): # Self-explanatory
    return_list = []
    for i in range(4):
        if user[i] in comp:
            if user[i] != comp[i]:
                return_list.append("WHITE")
            else:
                return_list.append("RED")
        else:
            return_list.append("BLACK")
    random.shuffle(return_list)
    print(return_list)
    return check_win(return_list)

def check_win(response_list):
    if response_list == ["RED", "RED", "RED", "RED"]:
        print("You win! congrats!")
        print("To play again, type play_game() into the console")
        return True

def play_game(): # Reset score & code, new game
    attempts = 5
    computer_list = create_comp_list()
    while True:
        if check_values(computer_list, get_guess()) == True:
            break
        else:
            attempts -= 1
            print("attempts left", attempts)
            print("----------")
            if attempts == 0:
                print("out of attempts! game over.")
                human_list = ""
                for i in range(4):
                    human_list += str(computer_list[i])
                print("My secret code was: " + human_list)
                print("To play again, type play_game() into the console")
                break

# Welcome screen:
print ("Welcome to Mastermind!")
print ("You have 5 chances to guess my secret 4-digit code!")
print ("Your guess must be 4 digits, and you can only use the same digit once!")
print ("All digits in the code must be between 1 and 7")
print("The guess format works in two ways: 'abcd' or 'a b c d'")
print ("----------")
print ("After each guess, I'll give you four responses in random order:")
print ("WHITE: One of your numbers is right, but it's not in the place!")
print ("RED: One of your numbers is right AND it's in the right place!")
print ("BLACK: One of your numbers is not the right number OR place.")
print ("----------")
print ("Attempts: 5")
play_game()
