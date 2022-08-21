from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/get_index_app')
def load_application():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()