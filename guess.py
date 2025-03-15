def get_guess():
    guess = int(input("Enter your guess: "))
    return guess

def main():
    guess = get_guess()
    if guess == 50:
        print("You win!")
    else:
        print("incorrect")
    print(guess)

main()