from flask import Flask
from flask_restful import Api, Resource
import random

answer = random.randint(1, 100)

app = Flask(__name__)
api = Api(app)

class Game(Resource):
    
    def get(self, num):
        if num == answer:
            return "Correct!"
        elif num < answer:
            return "Too low!"
        else:
            return "Too high!"

api.add_resource(Game, "/game/<int:num>")

if __name__ == "__main__":
    app.run(debug=True)