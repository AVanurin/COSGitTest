from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def show_main_page():
    return "Hello world!"

@app.route('/login')
def show_login_page():
    return render_template('login.html')


if __name__ == "__main__":
    app.run()
