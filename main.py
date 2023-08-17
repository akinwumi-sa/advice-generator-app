from flask import Flask, render_template
import requests

app = Flask(__name__)
API_ENDPOINT = "https://api.adviceslip.com/advice"


@app.route('/')
def home():
    response = requests.get(API_ENDPOINT)
    data = response.json()
    return render_template('index.html', advice=data)


if __name__ == "__main__":
    app.run(debug=True)
