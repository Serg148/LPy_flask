import random
import string


def generater_random_password(password_len=10) -> str:

     chars = string.digits + \
        string.ascii_letters + \
        string.punctuation

     result = ""
     for _ in range(password_len):
        result += random.choice(chars)
     return result
