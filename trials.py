var = 10

def func():
    global var
    var = 5

def check():
    global var
    print(var)

check()
func()
check()