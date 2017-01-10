#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import hashlib

# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }

db = {}

def register(username, password):
	db[username] = calc_md5(password + username + 'the-Salt')


def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()


def login(user, password):
    if db[user] == calc_md5(password + user + 'the-Salt'):
        # print("%s Login Success!" % user)
        return True
    else:
        # print("%s Login Fail!" % user)
        return False


def main():
    md5 = hashlib.md5()
    md5.update("how to use md5 in python hashlib?")
    print md5.hexdigest()

    # Test
    print("=============")
    users_reg = {'michael': '123456', 'bob': 'abc999', 'alice': 'alice2008'}
    for key in users_reg:
        print register(key, users_reg[key])
    print db
    users_login = {'michael': '889', 'bob': 'abc999', 'alice': 'alice2008'}
    for key in users_login:
        print login(key, users_login[key])


if __name__ == '__main__':
    main()
