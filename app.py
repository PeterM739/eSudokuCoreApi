"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

#from utils import *
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from generator import Generator
from checker import Checker

app = Flask(__name__)
cors = CORS(app)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/generate', methods=["GET"])
@cross_origin()
def generate():
    difficulty = request.args.get('difficulty')
    puzzle = Generator(difficulty)
   
    return jsonify(puzzle.generateSudoku())



#@app.route('/check', methods=["GET"])
#@cross_origin()
#def check():
#    solutionGrid = request.args.get('solutionGrid')
#    checkGrid = request.args.get('checkGrid')

#    return jsonify(Checker.checkSolution(checkGrid, solutionGrid))




if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run()
