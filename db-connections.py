import pyrebase

# config = {
#     "apiKey": "AIzaSyAiPuEH6tsR4h36GJKDzKtv87-2E9u0_oA",
#     "authDomain": "bon-voyage-d2ff1.firebaseapp.com",
#     "databaseURL": "https://bon-voyage-d2ff1.firebaseio.com",
#     "projectId": "bon-voyage-d2ff1",
#     "storageBucket": "bon-voyage-d2ff1.appspot.com",
#     "messagingSenderId": "38889641656",
#     "appId": "1:38889641656:web:de5b7cb9ee2da248ec064d",
#     "measurementId": "G-S2TSF9G04K"
# }

config = {
    "apiKey": "AIzaSyAiPuEH6tsR4h36GJKDzKtv87-2E9u0_oA",
    "authDomain": "bon-voyage-d2ff1.firebaseapp.com",
    "databaseURL": "https://bon-voyage-d2ff1.firebaseio.com",
    "storageBucket": "bon-voyage-d2ff1.appspot.com"
}

firebase = pyrebase.initialize_app(config)
#auth = firebase.auth()
db = firebase.database()
#storage = firebase.storage()

flights = db.child('flights').shallow().get()

print(flights)