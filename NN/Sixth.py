
class Bunny: #class declaration
    def __init__(self, name): #class constructor (code)
        self.name = name #attribute (data)

    def set_name(self, name): #method declaration (code)
        self.name = name #method implementation (code)

dave = Bunny('Kitten')
print(dave.name)