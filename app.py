from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def show_main_page():
    return "Hello world!"

@app.route('/serghome')
def show_main_page2():
    return "..."
  
@app.route('/login')
def show_login_page():
    return render_template('LoginPage.html')


if __name__ == "__main__":
    app.run()
