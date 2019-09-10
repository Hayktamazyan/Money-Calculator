class Student:
    activity = "Supermarket", "Cafeteria"
    weekdays = "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"

    def __init__(self, name, password, budget):
        self.name = name
        self.password = password
        self.budget = budget


    def get_personal_info(self):
        print(self.name)
        print(self.password)
        print(self.budget)
        print(self.activity)
        print(self.weekdays)



def main():
    user1 = Student("Gor", "Isoyan", 78)
    print("You input is: ".format(user1.__class__.activity))
    user1.get_personal_info()

main()
