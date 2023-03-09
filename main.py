import string
import random


def creat_password(length=8, upper=False, lower=False, digit=False, pun=False):
    pool = " "
    if upper:
        pool += string.ascii_uppercase
    if lower:
        pool += string.ascii_lowercase
    if digit:
        pool += string.digits
    if pun:
        pool += string.punctuation
    if pool == "":
        pool += string.ascii_letters

    return "".join(random.choices(pool, k=length))


if __name__ == '__main__':
    print(creat_password(12, upper=True))
    print(creat_password(12, upper=True, lower=True, digit=True, pun=True))
    print(creat_password(12, upper=True, lower=True, digit=True, pun=True))
    print(creat_password(12, upper=True, lower=True, digit=True, pun=True))
    print(creat_password(12, upper=True, lower=True, digit=True, pun=True))
    print(creat_password(12, upper=True, lower=True, digit=True, pun=True))
