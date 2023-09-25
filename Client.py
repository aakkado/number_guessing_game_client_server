import requests

BASE = "http://127.0.0.1:5000/"

guess = input("Enter your guess: ")

response = requests.get(BASE + "game/" + guess)

print(response.json())