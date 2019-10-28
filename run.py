from db_connections import find_flights
from conversions import find_flt_duration
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/flights-display', methods = ["GET", "POST"])
def show_flights():
    flights = []
    if request.method == 'POST':
        typ = request.form['type']
        print(typ)
        src = request.form['src']
        print(src)
        des = request.form['des']
        print(des)
        dep_date = request.form['dep_date']
        print(dep_date)
        ret_date = request.form['ret_date']
        print(ret_date)
        adults = request.form['adults']
        print(adults)
        kids = request.form['kids']
        print(kids)
        clas = request.form['class']
        print(clas)
        flights = find_flights(src, des, dep_date)
    return render_template('flights.html', flights = flights, clas = clas)

@app.route('/trains-display')
def show_trains():
    return render_template('trains.html')

@app.route('/hotels-display')
def show_hotels():
    return render_template('hotels.html')

@app.route('/checkout')
def checkout():
    return render_template('booking.html')

@app.errorhandler(404)
def error_handle(error):
    return 'Page not found'

if __name__ == '__main__':
    app.run(debug = True)
