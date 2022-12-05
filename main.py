
class User:
    def __init__(self, name, id):
        print("object created")
        self.name = name
        self.id = id
    def edit_id(self, id):
        self.id = id



user_1 = User("Uschi", "901")

user_1.edit_id("333")

print(user_1.name + " - " + user_1.id)

