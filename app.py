from flask import Flask

app = Flask(__name__)


@app.route('/')
def show_main_page():
    return "Hello world!"

@app.route('/Artem')
def show_main_page():
    return "Zdravstvuyte"


if __name__ == "__main__":
    app.run()
