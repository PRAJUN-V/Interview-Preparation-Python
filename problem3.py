# Generate a 6 digit otp in python

import random

def generate_otp(otp_length):
    otp = ''
    for _ in range(otp_length):
        otp += str(random.randint(0, 9))
    return otp

print(generate_otp(8))
