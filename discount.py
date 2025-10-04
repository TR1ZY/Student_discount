import random
# import getpass

def generate_discount_code():
    return str(random.randint(100000000, 999999999))

users = {
    "alice@school.edu": "12x129",
    "bob@college.edu": "1x1229",
    "carol@uni.edu": "122x29"
}

while True:
    email: str = input("Enter your email: ")

    if email in users:
        # print("Email Accepted")
        break
    else:
        print("Invalid Email")

while True:
    password = input('Enter your password: ')

    if password == users[email]:
        # print("Login Successful")
        print("Your discount code is", generate_discount_code())
        break
    else:
        print("Invalid Password")