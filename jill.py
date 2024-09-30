import argparse
import hashlib

parser = argparse.ArgumentParser(
                                 prog='Password Cracker',
                                 description='Cracks Passwords',
)

parser.add_argument('passfile')
parser.add_argument('dictfile')
args = parser.parse_args()

passwords = open(args.passfile, "r")
dictionary_file = open(args.dictfile, "r")

passwords_seperate = passwords.readlines()
dictionary_seperate = dictionary_file.readlines()

for hash in passwords_seperate:
    hash = hash.split(":")
    for psw in dictionary_seperate:
        if hashlib.sha256(psw.strip().encode()).hexdigest() == hash[1].strip():
            print(f'{hash[0]}:{psw.strip()}')

