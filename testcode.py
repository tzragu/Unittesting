import hashlib
import re


class InvalidEmail(Exception):
    pass


class InvalidSocial(Exception):
    pass


class InvalidPassword(Exception):
    pass

class Email:

    def __init__(self, email):
        search_Obj = re.search(r'[a-zA-Z]([a-zA-Z0-9]*)@([a-zA-Z0-9]*)\.edu|biz|com|gov', email, flags=0)
        if search_Obj is not None:
            self.email = search_Obj.group()
        else:
            raise InvalidEmail

    def __str__(self):
        return self.email


class SS:

    def __init__(self, social):
        search_Obj = re.search(r'[0-9]{3}-[0-9]{2}-[0-9]{4}', social, flags=0)
        if search_Obj is not None:
            self.social = social
        else:
            raise InvalidSocial

    def __str__(self):
        return self.social


class Hash:
    def __init__(self, passwd):
        if len(passwd) > 7:
            self.hash = self.generate_hash(passwd)
        else:
            raise InvalidPassword

    def __eq__(self, other):
        if isinstance(other, str):
            return self.hash == self.generate_hash(other)
        elif isinstance(other, Hash):
            return self.hash == other.hash
        else:
            return NotImplemented

    @staticmethod
    def generate_hash(passwd):
        """ This is NOT secure, a random salt should be added"""
        return hashlib.sha512(passwd.encode("utf-8")).hexdigest()

    def __str__(self):
        return self.hash
