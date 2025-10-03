import random

def generate_discount_code():
    return str(random.randint(100000000, 999999999))


email: str = input("Please enter your email: ")

if email.endswith(".edu"):
    discount = True
    print("Your student discount code is", generate_discount_code())
else:
    discount = False
    print("Please enter a valid student email address")