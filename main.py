from flask import Flask, request
from flask_restful import Api, Resource
import random

app = Flask(__name__)
api = Api(app)

class Game(Resource):
    def __init__(self):
        self.answer = random.randint(1, 1000)
        self.game_over = False

    def get(self, num):
        if self.game_over:
            return "Game over. Start a new game using /restart"
        
        if num == self.answer:
            self.game_over = True
            return "Correct! Type /restart to start a new game or /stop to stop."

        elif num < self.answer:
            return "Too low!"
        else:
            return "Too high!"

class Restart(Resource):
    def get(self):
        game.answer = random.randint(1, 1000)
        game.game_over = False
        return "New game started. Guess a number between 1 and 1000."

class Stop(Resource):
    def get(self):
        return "Game stopped. Goodbye!"

api.add_resource(Game, "/game/<int:num>")
api.add_resource(Restart, "/restart")
api.add_resource(Stop, "/stop")

if __name__ == "__main__":
    game = Game()
    app.run(debug=True)
