# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to=None, e_to=None, s_to=None, w_to=None):
        self.name = name
        self.descrition = description
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to
    def __str__(self):
        return f'{self.name} - {self.descrition}'
    def __repr__(self):
        return f'({repr(self.name)} - {repr(self.description)})'