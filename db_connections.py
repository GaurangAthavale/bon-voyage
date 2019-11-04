import pyrebase
import calendar

config = {
    "apiKey": "AIzaSyAiPuEH6tsR4h36GJKDzKtv87-2E9u0_oA",
    "authDomain": "bon-voyage-d2ff1.firebaseapp.com",
    "databaseURL": "https://bon-voyage-d2ff1.firebaseio.com",
    "storageBucket": "bon-voyage-d2ff1.appspot.com"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

def find_flights(src, dest, dep_date):
    year, month, date = (int(i) for i in dep_date.split('-'))     
    day = calendar.weekday(year, month, date)
    print('finding flights for',src, dest, dep_date, day)
    flights = db.child('flights').get()
    valids = []
    for fl in flights.each():
        info = fl.val()
        key = fl.key()
        # print(info['src'])
        # print(info['des'])
        # print(info['dep_days'])
        if info['src'] == src.upper() and info['des'] == dest.upper() and day in info['dep_days']:
            valids.append(info)
    print(len(valids))
    # print(valids)
    return valids

