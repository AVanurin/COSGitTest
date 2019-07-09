from flask import Flask

app = Flask(__name__)


@app.route('/')
def show_main_page():
    return "Hello world!"


@app.route('/Artem')
def show_my_next():
    return "Zdravstvuyte"

@app.route('/serghome')
def show_main_page2():
    return "..."

if __name__ == "__main__":
    app.run()
