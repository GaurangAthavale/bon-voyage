import pyrebase

config = {
    "apiKey": "AIzaSyAiPuEH6tsR4h36GJKDzKtv87-2E9u0_oA",
    "authDomain": "bon-voyage-d2ff1.firebaseapp.com",
    "databaseURL": "https://bon-voyage-d2ff1.firebaseio.com",
    "storageBucket": "bon-voyage-d2ff1.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

flights = db.child('flights').get()
for fl in flights.each():
    print(fl.key(),':',fl.val())