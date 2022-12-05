
class User:
    def __init__(self, name, id):
        print("object created")
        self.name = name
        self.id = id


    pass


user_1 = User("Uschi", "901")

print(user_1.name + " - " + user_1.id)

