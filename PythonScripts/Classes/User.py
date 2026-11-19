class User:
    def __init__(self, email, membership):
        """ Initialise user object """

        self.email = email
        self.membership = membership

    def get_email(self):
        return self.email

    def get_membership(self):
        return self.membership

    def set_email(self, email):
        self.email = email