# Please note that this code is made by me and I didn't use the AI tools only
# for search purpose.
# I worked very hard on this project to bring this up and I hope you like it!

import time
import random

monsters = [
    "troll", "dragon", "wicked fairy", "Zombie", "Vampire", "gorgon"
]

# The main function that I put in it the rest of the game functions to avoid
# using global variables and to make sure that the variables are in the scope
# of the game function so that add more security.


def game():
    time_delayed = 2
    player_score = 0
    never_been_to_the_cave = True

    # This function to make delay in the message to seem more dramatic.
    # I used the join function to avoid printing the quotes and parentheses.
    def print_pause(*m):
        print(" ".join(m))
        time.sleep(time_delayed)

    # This is the most important function in the game as it takes four
    # parameters from another function. It takes two questions to ask the
    # player and it takes two functions to execute by every choice the player
    # will provide. I used the nonlocal keyword to declare the player score
    # variable inside the nested function.
    def ask_player(choice1, choice2, func1, func2):
        nonlocal player_score
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
        else:
            print_pause("Invalid input!")
            return ask_player(choice1, choice2, func1, func2)

    # This function I call it when the player defends the monster.
    # It asks for the way that the player will defend itself
    # and if the way is to cast a spell it will check if the wand is rusty
    # or not.
    def defend(way, is_rusty=True):
        nonlocal player_score
        monster = random.choice(monsters)
        if way == "spell":
            if is_rusty:
                print_pause("You do your best...")
                print_pause(
                    f"but your rusty old magic wand is no match for the "
                    f"{monster}."
                )
                print_pause("You have been turned into a frog!")
                player_score -= 1000
                print_score()
                replay()
            else:
                print_pause(
                    "As the dragon moves to cast a spell, "
                    "you raise your new Wand of Ogoroth."
                )
                print_pause(
                    "The Wand of Ogoroth shines brightly in your hand "
                    "as you brace yourself for the spell."
                )
                print_pause(
                    "But the dragon takes one look at your shiny new Wand "
                    "and runs away!."
                )
                print_pause(
                    "You have rid the town of the dragon. YOU ARE VICTORIOUS!"
                )
                player_score += 1000
            print_score()
            replay()

        elif way == "run":
            print_pause(
                "You run back into the field. Luckily, "
                "you don't seem to have been followed."
            )
            player_score += 100
            print_score()
            field()

    # This is the function that I call when the player goes to the cave.
    # If he went before the never_been_to_the_cave will be false so the game
    # avoid repeating. At the end of entering the cave, the game will call
    # the field function to return the player to the field.
    def cave():
        nonlocal player_score, never_been_to_the_cave
        if never_been_to_the_cave:
            print_pause("You peer cautiously into the cave.")
            print_pause("It turns out to be only a very small cave.")
            print_pause("Your eye catches a glint of metal behind a rock.")
            print_pause(
                "You discard your rusty old magic wand and take the "
                "Wand of Ogoroth with you."
            )
            print_pause("You walk back out to the field.")
            player_score += 1000
            never_been_to_the_cave = False
            print_score()
        else:
            print_pause("You peer cautiously into the cave.")
            print_pause(
                "You've been here before, and gotten all the good stuff. "
                "It's just an empty cave now."
            )
            print_pause("You walk back out to the field.")
            print_score()
        field()

    # The field function just calls the ask_player function and requests the
    # player for his choices.
    def field():
        ask_player(
            "knock on the door of the house.",
            "peer into the cave.",
            house,
            cave
        )

    # The house function has a random monster every time the game is played.
    # It checks if the player had gone to the cave or not
    # and it calls the defend function and the defend function will decide
    # if the player won or not.
    def house():
        monster = random.choice(monsters)
        print_pause("You approach the door of the house.")
        print_pause(
            f"You are about to knock when the door opens and out steps a "
            f"{monster}."
        )
        print_pause(f"Eep! This is the {monster}'s house!")
        print_pause(f"The {monster} finds you!!")
        if never_been_to_the_cave:
            print_pause(
                "You feel a bit underprepared for this, "
                "what with only having a tiny, rusty old magic wand."
            )
            ask_player(
                "cast a spell",
                "run away",
                lambda: defend("spell", True),
                lambda: defend("run")
            )
        else:
            print_pause(
                "You feel better prepared with your new Wand of Ogoroth."
                )
            ask_player(
                "cast a spell",
                "run away",
                lambda: defend("spell", False),
                lambda: defend("run")
            )

    def print_score():
        nonlocal player_score
        print(f"{'-'*30}(Your Score is: {player_score}){'-'*30}")

    def replay():
        print_pause("Would you like to play again?")
        play_again = input("Enter Y for yes or N for no:")
        if play_again.lower() == "y":
            print_pause("Excellent! Restarting the game...")
            game()
        else:
            print_pause("Thank you for playing!")

    # These are the lines printed when we start the game.
    print_score()
    print_pause(
        "You find yourself standing in an open field, "
        "filled with grass and yellow wildflowers."
    )
    print_pause(
        "Rumor has it that a wicked fairy is somewhere around here, "
        "and has been terrifying the nearby village."
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(
        "In your hand you hold your trusty (but not very effective) "
        "magic wand."
    )

    field()


game()
