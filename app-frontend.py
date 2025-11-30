from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    try:
        response = requests.get('http://backend-service:5001/api/message')
        data = response.json()
        message = data['message']
    except:
        message = "Could not connect to backend"
    
    return f"<h1>Frontend Microservice</h1><p>{message}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)