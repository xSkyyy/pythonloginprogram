import time
print("loading vital systems. please wait.")
time.sleep(15)
print("checking hardware. please wait.")
time.sleep(15)
print("welcome to windows 10")
time.sleep(2)
print("Please input your login credentials so we can log you in")
time.sleep(2)
loggedin = False
username = "mattc"
password = "Password"

while loggedin == False:
    inputusername = input("Username:")
    time.sleep(3)
    inputpassword = input("Password:")
    if inputusername == username and inputpassword == password:
        print("Checking credentials...")
        time.sleep(5)
        print("Loading default programs")
        time.sleep(2)
        print("Preparing GUI...")
        time.sleep(2) 
        loggedin = True
    else:
        print("Checking credentials...")
        time.sleep(3)
        print("Please try again")
        loggedin = False
