# attributes: name, age, genre, hobby, daily routine, things i ilove, things i hate, future profession
# methods: 


class aboutMe:
    def __init__(self, name, completeName, age, gender, hobby):
        self.name = name
        self.completeName = completeName
        self.age = age
        self.gender = gender
        self.hobby = hobby
    def introduce(self):
        print(f"My complete name is {self.completeName}.")
        print(f"Though, you MUST call me {self.name}.")
    def show_hobby(self):
        print(f"My hobby is {self.hobby}.")
    def dailyRoutine(self, routine1, routine2, routine3, routine4):
        print(f"My daily routine is I {routine1} every morning, then shortly after that I {routine2}, and finally I {routine3} at night, and sleep at night at {routine4} everyday.")
    def thingsILove(self, love1, love2, love3):
        print(f"I love to {love1}, {love2}, and {love3} pretty much.")
    def thingsIHate(self, hate1, hate2, hate3):
        print(f"I hate {hate1}, {hate2}, and {hate3} so much.")
    def futurePlan(self, plan, live):
        print(f"In the future, I want to be a {plan} and live in {live}.")

info = aboutMe("Rofi", "Muhammad Dafi Arib Asyrofi", 18, "Men", "Coding")


print(f"\n{"About Me":-^80}")
info.introduce()
info.show_hobby()
info.dailyRoutine("code", "code", "code", "9pm")
info.thingsILove("code", "listen to music", "watch anime")
info.thingsIHate("dirty things", "messy things", "something that is not in the right places")
info.futurePlan("Machine Learning Engineer", "Japan")

