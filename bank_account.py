import hashlib
import os.path
accounts = {}
salts = []
num = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
C = ('C')
L = ('L')
Q = ('Q')
def get_salt():
    f = open("salts.txt", "r")
    for line in f:
        salts.append(line.strip("\n"))

def salt_password(password):
    indexA = ord("a")
    last_letter = password[-1]
    if not last_letter.isalnum() :
        index = 0
    elif last_letter.isnumeric():
        index = int(last_letter)
    else:
        last_letter1 = last_letter.lower()
        index1 = ord(last_letter1)
        index = index1 - indexA
    return salts[index]

def read_file():
    if not os.path.isfile("accounts.txt"):
        return
    f = open("accounts.txt", "r")
    for line in f:
        
        words = (line.split(" "))
        words.pop()
        username = words[0]
        password = words[1]
        PIN = words[2]
        balance1 = int(words[3])
        currency1 = words[4]
        balance2 = int(words[5])
        currency2 = words[6]
        accounts.update({words[0] : [password, PIN, balance1, currency1, balance2, currency2]})
        
def write_file():
    f = open("accounts.txt", "w")
    for username in accounts:
        f.write(username + " ")
        info = accounts[username]
        for item in info:
            f.write(str(item) + " ")
        f.write("\n")
    f.close()

def hasher(password, salt):
    b = bytes(password + salt, 'utf-8')
    m = hashlib.sha256(b)
    m = m.hexdigest()
    return m



currency1 = ('USD')
currency2 = ('euro')
def logout():
    print("loged of")
    message = input("Enter C to creat an account or enter L to login your account")
    while message != Q:
        if message == C:
            username =input("New username")
            if accounts.get(username):
                print("username already exist")
                message = input("Enter C to creat an account or enter L to login your account")
            else:
                password =input("New password")
                salt = salt_password(password)
                password = hasher(password, salt)
                PIN =input("New PIN")
                accounts.update({username : [password, PIN, 0, currency1, 0, currency2]})
                message = input("Enter C to creat an account or enter L to login your account")
                write_file()
        elif message == L:
            login()
def transfer():
    message =input("to transfer money to another account press A, to transfer money to your account press M")
    if message == 'A':
        message =input("to transfer USD to another account press UA, to transfer euro to another account press EA")
        if message == 'UA':
            message =input("Which account do you want to transfer money to?")
            message1 =int(input("How much money do you want to transfer"))
            if accounts[username][2] > message1 or accounts[username][2] == message1:
                accounts[message][2] += message1
                accounts[username][2] -= message1
                print(accounts[username][2])
                print("Thank you for chosing us for your bank")
                message =input("To log off press LO, to transfer money press T, to look at your account info press I, to change your money currency to USD press U, to change your money currency to euro press E.")
            else:
                print("You do not have that much money in your account")
                message =input("To log off press LO, to transfer money press T, to look at your account info press I, to change your money currency to USD press U, to change your money currency to euro press E.")
        elif message == 'EA':
            message =input("Which account do you want to transfer money to?")
            message1 =int(input("How much money do you want to transfer"))
            if accounts[username][4] > message1 or accounts[username][4] == message1:
                accounts[message][4] += message1
                accounts[username][4] -= message1
                print(accounts[username][4])
                print("Thank you for chosing us for your bank")
                message =input("To log off press LO, to transfer money press T, to look at your account info press I, to change your money currency to USD press U, to change your money currency to euro press E.")
            else:
                print("You do not have that much money in your account")
                message =input("To log off press LO, to transfer money press T, to look at your account info press I, to change your money currency to USD press U, to change your money currency to euro press E.")
    elif message == 'M':
        message =input("to transfer USD to your account press UM, to transfer euro to your account press EM.")
        if message == 'UM':
            amt = int(input("How much money do you want to transfer"))
            print("Put money into ATM")
            accounts[username][2] += amt
            print(accounts[username][2])
            print("Thank you for chosing us for your bank")
            message =input("To log off press LO, to transfer money press T, to look at your account info press I, to change your money currency to USD press U, to change your money currency to euro press E.")
        elif message == 'EM':
            amt = int(input("How much money do you want to transfer"))
            print("Put money into ATM")
            accounts[username][4] += amt
            print(accounts[username][4])
            print("Thank you for chosing us for your bank")
            message =input("To log off press LO, to transfer money press T, to look at your account info press I, to change your money currency to USD press U, to change your money currency to euro press E.")
def info():
    print(accounts[username])
    message =input("To log off press LO, to transfer money press T, to look at your account info press I, to change your money currency to USD press U, to change your money currency to euro press E.")
def eurochange():
    message = int(input("How much USD do you want to change?"))
    if accounts[username][4] >= message:
        accounts[username][4] += 85 * message / 100
        accounts[username][2] -= message
        print(accounts[username][4])
        print(accounts[username][5])
        print(accounts[username][2])
        print(accounts[username][3])
        message =input("To log off press LO, to transfer money press T, to look at your account info press I, to change your money currency to USD press U.")
    else:
        print("You do not have that much money in your account")
        message =input("To log off press LO, to transfer money press T, to look at your account info press I, to change your money currency to USD press U, to change your money currency to euro press E.")
def USDchange():
    message = int(input("How much euro do you want to change?"))
    if accounts[username][2] >= message:
        accounts[username][2] += 117 * message / 100
        accounts[username][4] -= message
        print(accounts[username][2])
        print(accounts[username][3])
        print(accounts[username][4])
        print(accounts[username][5])
        message =input("To log off press LO, to transfer money press T, to look at your account info press I, to change your money currency to euro press E.")
    else:
        print("You do not have that much money in your account")
        message =input("To log off press LO, to transfer money press T, to look at your account info press I, to change your money currency to USD press U, to change your money currency to euro press E.")


def login():
    username =input("Your username")
    if not accounts.get(username):
        print("Invalid username")
        return
    elif accounts.get(username):
        for i in range(0,6):
            password =input("Your password")
            password = hasher(password, salt_password(password))
            if i == 5:
                print("Locked out sucks 2 b u")
                break
            if password == accounts[username][0]:
                print("Welcome " + username + "!")
                message =input("To log off press LO, to transfer money press T, to look at your account info press I, to change your money currency to USD press U, to change your money currency to euro press E.")
                while message != Q:
                    if message == "LO":
                        logout()
                    if message == "T":
                        transfer()
                    if message == "E":
                        eurochange()
                    if message == "U":
                        USDchange()
                    if message == "I":
                        info()
                            
                        
                              
        else:
            print("Wrong password")

get_salt()        
read_file()
message = input("Enter C to creat an account or enter L to login your account")
while message != Q:
    if message == C:
        username =input("New username")
        if accounts.get(username):
            print("username already exist")
            message = input("Enter C to creat an account or enter L to login your account")
        else:
            password =input("New password")
            salt = salt_password(password)
            password = hasher(password, salt)
            PIN =input("New PIN")
            accounts.update({username : [password, PIN, 0, currency1, 0, currency2]})
            message = input("Enter C to creat an account or enter L to login your account")
            write_file()
    elif message == L:
        login()
