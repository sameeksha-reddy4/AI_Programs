import random
import string

print("CAPTCHA Verification System\n")

def generate_captcha(length=6):
    chars = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(chars) for _ in range(length))
    return captcha

captcha = generate_captcha()

print("CAPTCHA:", captcha)

user_input = input("Enter CAPTCHA exactly as shown: ")

if user_input == captcha:
    print("\nAccess Granted — You are HUMAN ✅")
else:
    print("\nAccess Denied — Verification Failed ❌")