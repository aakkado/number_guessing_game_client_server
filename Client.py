import requests

BASE = "http://127.0.0.1:5000/"

while True:
    guess = input("Enter your guess (or 'q' to quit): ")

    if guess.lower() in ['q', 'quit']:
        print("Exiting the game. Goodbye!")
        break

    try:
        guess = int(guess)
        response = requests.get(BASE + "game/" + str(guess))
        print(response.json())

        if response.json() == "Correct! Type /restart to start a new game or /stop to stop.":
            restart = input("Do you want to restart the game? (y/n): ")
            if restart.lower() == 'y':
                response = requests.get(BASE + "restart")
                print(response.json())
            else:
                print("Goodbye!")
                break

    except ValueError:
        print("Invalid input. Please enter a valid number or 'q' to quit.")
