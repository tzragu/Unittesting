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
        searchobj = re.search(r'^[a-zA-Z]([a-zA-Z0-9]*)@[a-zA-Z]([a-zA-Z0-9\.]*)\.(edu|biz|com|gov)$', email, flags=0)
        if searchobj is not None:
            self.email = email
        else:
            raise InvalidEmail

    def __str__(self):
        return self.email


class SS:

    def __init__(self, social):
        search_obj = re.search(r'^(?!219-09-9999|078-05-1120)(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}$',
                               social, flags=0)
        if search_obj is not None:
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
