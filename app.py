from flask import Flask

app = Flask(__name__)


@app.route('/')
def show_main_page():
    return "Hello world!"

@app.route('/home')
def show_home():
    return "Hello from your pythony pupil!"

if __name__ == "__main__":
    app.run()
