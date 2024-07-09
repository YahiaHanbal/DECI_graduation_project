import time
import random

time_delayed = 0.5
player_score = 0
NeverBeenToTheCave = True

in_game = True
monsters = ["troll", "dragon", "wicked fairy", "Zombie", "Vampire", "gorgon"]


def print_pause(*m):
    #join function is used to avoid printing of the parentheses and quotes.
    print(" ".join(m))
    time.sleep(time_delayed)


def ask_player(choice1: str, choice2: str, func1, func2):
    global player_score

    print_pause("\nWhat would you like to do?")
    print(f"(Enter 1 to {choice1} or 2 to {choice2}).")

    player_choice = input()
    if player_choice == "1" or player_choice == "2":
        if player_choice == "1":
            func1()
            player_score += 100
        else:
            func2()
            player_score += 100
    # this will loop until the player input a valid option.
    else:
        print_pause("Invalid input!")
        return ask_player(choice1, choice2, func1, func2)


def defend(way, isRusty=True):
    global player_score
    if way == "spell":
        if isRusty is True:
            print_pause("You do your best...")
            print_pause(f"but your rusty old magic wand is no match for the {monster}.")
            print_pause("You have been turned into a frog!")
            player_score -= 1000
            print(f"-"*30+"(Your Score is: {player_score})"+"-"*30)
            replay()
        else:
            print_pause("As the dragon moves to cast a spell, you raise your new Wand of Ogoroth.")
            print_pause("The Wand of Ogoroth shines brightly in your hand as you brace yourself for the spell.")
            print_pause("But the dragon takes one look at your shiny new Wand and runs away!.")
            print_pause("You have rid the town of the dragon. YOU ARE VICTORIOUS!")
            player_score += 1000
        print(f"-"*30+"(Your Score is: {player_score})"+"-"*30)
        replay()

    elif way == "run":
        print_pause("You run back into the field. Luckily, you don't seem to have been folowed.")
        player_score += 100
        field()
    # Things that happen when the player is approached by an enemy  


def cave():
    # Things that happen to the player goes in the cave
    global player_score
    global NeverBeenToTheCave
    if NeverBeenToTheCave is True:
        print_pause("You peer cautiusly into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You discard your rusty old magical wand and take the wand of ogoroth with you.")
        print_pause("You walk back out to the field.")
        player_score += 1000
        print(f"-"*30+"(Your Score is: {player_score})"+"-"*30)
    else:
        print_pause("You peer cautiusly into the cave.")
        print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
    field(False)


def field(DidYouEnteredTheCave=True):
    # i want to make a boolean that checks if the person had take the things from cave or not 
    global NeverBeenToTheCave
    NeverBeenToTheCave = DidYouEnteredTheCave
    # Things that happen when the player runs back to the field
    ask_player("knock on the door of the house.", "peer into the cave.",lambda: house(NeverBeenToTheCave), cave)


def house(withRustyWand=True):
    global monster
    monster = random.choice(monsters)    
    # Things that happen to the player in the house
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens and out steps a {monster}.")
    print_pause(f"Eep! This is the {monster}'s house!")
    print_pause(f"The {monster} finds you!!")
    if withRustyWand is True:
        print_pause("You feel a bit under prepared for this, what with only having a tiny, rusty old magic wand.")
        ask_player("cast a spell", "run away",lambda: defend("spell", True),lambda: defend("run"))
    else:
        print_pause("You feel a bit under prepared for this, what with only having a tiny, rusty old magic wand.")
        ask_player("cast a spell", "run away",lambda: defend("spell", False),lambda: defend("run"))

        
def replay():
    print_pause("Would you like to play again?")
    play_again = input("Enter Y for yes or N for no:")
    if play_again == "Y" or play_again == "y":
        print_pause("Excellent! Restarting the game...")
        return game()
    else:
        print_pause("Thank you for playing!")


def game():
    player_score = 0
    print(f"-"*30+"(Your Score is: {player_score})"+"-"*30)
    print_pause("You find yourself standing in an open field, filled with grass",
                "and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairy is somewhere around here,",
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)",
                 "magic wand.")


    ask_player("knock on the door of the house.", "peer into the cave.", house, cave)
    print(f"-"*30+"(Your Score is: {player_score})"+"-"*30)
game()