from blackjack import BlackjackGame

def main():
    print("Welcome to Terminal Blackjack!")
    while True:
        game = BlackjackGame()
        game.play()
        
        play_again = input("\nPlay another hand? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
