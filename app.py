from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def show_main_page():
    return "Hello world!"


@app.route('/Artem')
def show_my_next():
    return "Zdravstvuyte"


@app.route('/serghome', methods=["POST"])
def show_main_page2():
    return ")))"


@app.route('/login', methods=["GET"])
def show_login_page():
    return render_template('LoginPage.html')


if __name__ == "__main__":
    # Запуск приложения!
    app.run()
