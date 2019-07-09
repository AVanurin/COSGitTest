from flask import Flask

app = Flask(__name__)


@app.route('/')
def show_main_page():
    return "Hello Natasha from your pythony husb!"


if __name__ == "__main__":
    app.run()