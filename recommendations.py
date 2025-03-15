def main():
    
    difficulty = input("Difficult or Casual?").strip().lower()
    players = input("Multiplayer or single-player?").strip().lower()

    if difficulty == "difficult":
        if players == "multiplayer":
            game("Poker")
        elif players == "single-player":
            game("Solitaire")
        else:
            print(" Enter a valid number of players")
    elif difficulty == "casual":
        if players == "multiplayer":
            game("Hearts")
        elif players == "single-player":
            game("Clock")
        else:
            print("Enter a valid number of players")
    else:
        print("Enter a valid difficulty")

def game(game_name):
    print("You might like: " + game_name)

main()