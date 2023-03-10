import string
import random
import argparse


def creat_passwored(lentgh=8, upper=False, lower=False, digit=False, pun=False):
    pool = " "
    if upper:
        pool += string.ascii_uppercase
    if lower:
        pool += string.ascii_lowercase
    if digit:
        pool += string.digits
    if pun:
        pool += string.punctuation,
    if pool == " ":
        pool += string.ascii_letters
    return "".join(random.choices(pool, k=lentgh))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='creator password',
    )
    parser.add_argument('length', type=int, help='Enter the Lentgh of password')
    parser.add_argument('-u', '--upper', help='use upper case ', action='store_true')
    parser.add_argument('-l', '--lower', help='use lower case', action='store_true')
    parser.add_argument('-d', '--digit', help='use digit', action='store_true')
    parser.add_argument('-p', '--pun', help='use pun', action='store_true')

    args = parser.parse_args()
    print(creat_passwored(args.length, args.upper, args.lower, args.digit, args.pun))
