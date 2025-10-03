import random

def generate_discount_code():
    return str(random.randint(100000000, 999999999))

allowed_domains = ["@school.edu", "@stu.edu", "@.edu", "@college.edu", "@uni.edu"]

while True:
    email: str = input("Please enter your email: ")
    if any (email.endswith(domain) for domain in allowed_domains):
        discount = True
        print("Your student discount code is", generate_discount_code())
        break
    else:
        discount = False
        print("Please enter a valid student email address")

