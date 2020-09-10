import random
import string
import requests

from faker import Faker


def generater_random_password(password_len=10) -> str:
    chars = string.digits + \
            string.ascii_letters + \
            string.punctuation
    result = ""
    for _ in range(password_len):
        result += random.choice(chars)
    return result


def reading_requirements() -> str:
    file = open("requirements.txt")
    file = file.read()
    return file


fake = Faker()
def generate_users(users) -> str:
    users_list = ""
    for _ in range(users):
        users_list += f"({fake.first_name()}  {fake.ascii_email()})"
    return users_list

def people_in_space():
    r = requests.get('http://api.open-notify.org/astros.json')
    return str(r.json()["number"])
