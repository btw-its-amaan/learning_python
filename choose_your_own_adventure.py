name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You find yourself at the edge of an ancient forest, with a worn dirt path that splits in two directions. Do you choose to go left towards the shadowy woods, or right towards the misty hills? Type 'left' or 'right': ").lower()

if answer == "left":
    answer = input("You enter the shadowy woods and eventually reach a wide, rushing river. The current looks strong. Do you try to swim across, or take the long path to walk around? Type 'walk' to walk around or 'swim' to swim across: ")

    if answer == "swim":
        print("You dive in, but the current is stronger than you expected. Suddenly, a massive crocodile emerges and you are devoured before you can escape. Game over.")
    elif answer == "walk":
        print("You decide to walk around the river. The journey is exhausting, water is scarce, and after many hours you collapse from dehydration. You lose the game.")

    else:
        print("Not a valid option. You wander aimlessly and lose.")

elif answer == "right":
    answer = input("Heading toward the misty hills, you come upon a creaky rope bridge spanning a deep chasm. The bridge sways in the wind. Do you cross the bridge or return the way you came? Type 'cross' to cross the bridge or 'back' to go back: ")

    if answer == "back":
        print("You turn back, but lose your way in the endless fog. You lose.")
    elif answer == "cross":
        answer = input("You cross the shaky bridge safely and, on the other side, encounter a hooded wanderer by a campfire. Do you choose to speak with them? Type 'yes' to talk or 'no' to walk away: ")
        
        if answer == "yes":
            print("The wanderer smiles, seeing your courage. They hand you a mysterious pouch filled with gold and wish you well. You win!")
        elif answer == "no":
            print("You ignore the wanderer, but as you continue on your way, you become hopelessly lost in the hills. You lose.")

        else:
            print("Not a valid option. You hesitate too long and the opportunity is lost. You lose.")

else:
    print("Not a valid option. You sit down at the crossroads and the adventure ends here.")

print("Thank you for playing!")
