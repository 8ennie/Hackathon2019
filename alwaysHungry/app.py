from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('ChatMessage.html', username="", message="Welcome to Always Hungry. Im am Stewie, your personal Guide throw the Always Hungry World.")


if __name__ == '__main__':
    app.run(debug=True)
