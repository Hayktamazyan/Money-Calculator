import json
print('\n   Welcome to MoneySaver program ')
print('\n   Please enter your option ')


class Student:

    user = {}
    new_data = {}


    def student(self):
        with open("main.json") as data_file:
            activities = json.load(data_file)
        return activities['student']['activity']

    def __init__(self, name, password):
        self.name = name
        self.password = password
        Student.user['name'] = str(input("\nPlease enter your name: "))
        Student.user['password'] = str(input("\nPlease enter your password: "))


    @classmethod
    def set_up_json(cls):
        with open("main.json") as data_file:
            cls.file = json.load(data_file)
            cls.weekdays = cls.file['student']['weekdays']
            cls.activity = cls.file['student']['activity']
            cls.money = cls.file['student']['budget']
            return cls.weekdays, cls.activity, cls.money


class Activity(Student):
    def input_activity(self):
        activity = input("\nPlease choose one of the activities: ")
        with open("main.json", "r") as file:
            main_dict = json.load(file)
        while True:
            if activity in main_dict:
                return activity
            else:
                print("You have a wrong input, Try again: ")




class Weekday(Student):
    def input_weekdays(self):
        data = input("Please choose your weekday")
    pass


def main():
    print("\n   Here are the activities: ")
    student = Student.set_up_json()
    student1 = Student(Activity.input_activity([]))

    # print(student)
    print(student1)


main()





















