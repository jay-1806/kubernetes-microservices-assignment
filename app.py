# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "<h1>Hello! My Simple App is Running!</h1>"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
    
    
from flask import Flask
import random

app = Flask(__name__)

quotes = [
    # "Keep going!",
    # "You can do it!",
    # "Every step counts!",
    # "Believe in yourself!",
    # "Success is near!",
    "Stay positive!",
    "Make it happen!",      
    "Dream big!",
    "Never give up!",
    "Stay focused!"
]

@app.route('/')
def home():
    return f"<h1>{random.choice(quotes)}</h1>"

if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0', port=5000)
