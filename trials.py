# var = 10

# def func():
#     global var
#     var = 5

# def check():
#     global var
#     print(var)

# check()
# func()
# check()

from random import randint

c_names=[['Nikhil Bharadwaj'],['Gaurang Athavale'],['Kapil Sharma'],['Rohit Sharma'],['Virat Kohli'],['Cheteshwar Pujara'],['Swapnil Pawar'],['Gaurav Bhagwanani'],['Dhruvil Pujara'],['Deep Dama'],['Mihir Gada']]

cards = [['Visa','4'],['Mastercard','55'],['American Express','34'],['Maestro','6759']]


def cc():
    for i in range(len(c_names)):
        data = dict()
        data['name'] = c_names[i][-1]
        x = randint(0,3)
        c_names[i].append(cards[x][0])
        data['card_name'] = c_names[i][-1]
        c_names[i].append(cards[x][1])
        # print(c_names[i])
        while(len(c_names[i][-1])!=16):
            c_names[i][-1]=c_names[i][-1]+str(randint(0,9))
        data['card_no'] = c_names[i][-1]
        m = randint(1,12)
        y = randint(20,25)
        c_names[i].append('{:02d}'.format(m))
        data['card_month'] = c_names[i][-1]
        c_names[i].append('{:02d}'.format(y))
        data['card_year'] = c_names[i][-1]
        c_names[i].append(str(randint(100,999)))
        data['cvv'] = c_names[i][-1]
        # db.child('pay-cards').child(data['card_no']).set(data)
        print(data)

cc()