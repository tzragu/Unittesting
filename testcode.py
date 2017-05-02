class InvalidEmail(Exception):
    pass


class InvalidSocial(Exception):
    pass


class InvalidPassword(Exception):
    pass


class Email:

    def __init__(self, email):
        if "@" in email:
            self.email = email
        else:
            raise InvalidEmail

    def __str__(self):
        return self.email


class SS:

    def __init__(self, social):
        if "-" in social:
            self.social = social
        else:
            raise InvalidSocial


class Hash:
    x = 0

    def __init__(self, passwd):
        if len(passwd) > 1:
            self.hash = self.generate_hash(passwd)
        else:
            raise InvalidPassword

    def __eq__(self, passwd):
        return self.hash == self.generate_hash(passwd)

    @staticmethod
    def generate_hash(passwd):
        Hash.x += 1
        return Hash.x
