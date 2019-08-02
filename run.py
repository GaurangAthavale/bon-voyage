from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/flights')
def flights_page():
    return render_template('flights.html')

if __name__ == '__main__':
    app.run(debug = True)
