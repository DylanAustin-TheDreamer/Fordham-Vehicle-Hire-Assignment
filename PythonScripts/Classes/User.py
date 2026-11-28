class User:
    def __init__(self, membership):
        """ Initialise user object """

        self.membership = membership

    def get_membership(self):
        return self.membership