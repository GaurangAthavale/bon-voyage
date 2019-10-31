[![made-with-python](https://img.shields.io/badge/made%20with-python-red.svg)](https://www.python.org/)  [![powered-by-flask](https://img.shields.io/badge/powered%20by-flask-blue.svg)](http://flask.palletsprojects.com/en/1.1.x/) 

# bon-voyage
Web application to help users see and book flights, trains and hotels for their journey

## Description
The website has a user interface where the users can view avaialable flights, trains or hotels and book them for their journey. To render data to the frontend, this project demonstrates the use of both:
* Interacting with a database
* Scraping realtime data from the web

## Features
* Shows the users a list of available flights, hotels or trains based on search parameters
* Can be filtered on the basis of price, duration
* Implemented a [firebase](https://firebase.google.com/) database for flights
* For trains and hotels, realtime data is scraped

## Installation
Clone the repository to your local device
```
$ pip install -r requirements.txt
$ python run.py
```
Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and **have fun**.

## Limitation
* Currently, the flights database has routes between only a few major airports, to demonstrate the connectivity of firebase with flask. However, it can be extended for more airports and populated easily.

## Screenshots

* Home
![home](https://github.com/g-bhagwanani/bon-voyage/blob/master/static/images/screenshots/1-home.png)

* Login and Sign-up
![login](https://github.com/g-bhagwanani/bon-voyage/blob/master/static/images/screenshots/2-login.png)
![signup](https://github.com/g-bhagwanani/bon-voyage/blob/master/static/images/screenshots/3-signup.png)

* Find
![flights](https://github.com/g-bhagwanani/bon-voyage/blob/master/static/images/screenshots/4-find-flights.png)
![trains](https://github.com/g-bhagwanani/bon-voyage/blob/master/static/images/screenshots/5-find-trains.png)

* View
![flights](https://github.com/g-bhagwanani/bon-voyage/blob/master/static/images/screenshots/6-view-flights.png)

* Checkout
![deets](https://github.com/g-bhagwanani/bon-voyage/blob/master/static/images/screenshots/7-checkout.png)
![visa detect](https://github.com/g-bhagwanani/bon-voyage/blob/master/static/images/screenshots/8-visa.png)
![mastercard detect](https://github.com/g-bhagwanani/bon-voyage/blob/master/static/images/screenshots/9-mastercard.png)
