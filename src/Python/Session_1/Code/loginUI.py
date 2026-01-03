import random

def login_sys ():
    user = "test"
    password = "1234"
    while True:
        x = input ("Enter Your Username:  ")
        if x == user:
            y = input ("Enter Your password:  ")
            if y == password:
                v = random.randrange (100, 999)
                print (f"Your Code is {v}")
                while True:
                    e = int (input ("Enter Your code: "))
                    if e == v:
                        print ("Access Success!!")
                        break
                    else:
                        print ("Code is Incorrect!!!!, please try again")
                        break
                break
            else:
                print ("Password is Incorrect!!!!, please try again")
                continue
        else:
            print ("username is Incorrect!!!!, please try again")
            continue