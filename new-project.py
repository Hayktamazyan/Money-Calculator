import json
print('\n   Welcome to MoneySaver program ')
print('\n   Please enter your option ')


class Student:

    user = {}
    new_data = {}



    def __init__(self, name, password, data):
        self.name = name
        self.password = password
        self.data = data
        Student.user['name'] = str(input("\nPlease enter your name: "))
        Student.user['password'] = str(input("\nPlease enter your password: "))
        Student.new_data['data'] = data

    @classmethod
    def student(cls):
        with open("main.json") as data_file:
            cls.activities = json.load(data_file)
        return cls.activities['student']['activity']

    @classmethod
    def set_up_json(cls):
        with open("main.json") as data_file:
            cls.file = json.load(data_file)
            cls.weekdays = cls.file['student']['weekdays']
            cls.activity = cls.file['student']['activity']
            cls.money = cls.file['student']['budget']
            return cls.weekdays, cls.activity, cls.money

    @staticmethod
    def input_money():
        while True:
            money = input("\nPlease enter the amount of money: ")
            temp = money.replace('.', '', 1)
            if temp.isdigit():
                money = float(money)
                return money
            else:
                print("\nSomething went wrong, try again:")

    @classmethod
    def info_input(cls):
        for j in cls.['student']['activity']:
            print(j)
        Student.new_data = Activity.input_activity()
        for i in cls.data['student']['weekdays']:
            print(i)
        Student.new_data = Weekday.input_weekdays()
        for a in cls.data['student']['money']:
            print(a)
        Student.new_data = Student.input_money()
        with open('data_saver.json', 'r') as file:
            cls.data = json.load(file)
        with open('data_saver.json', 'w') as f:
            f.write(json.dumps(cls.data))

    @classmethod
    def action(cls):
        cls.actions = int(input("\n1 - press for adding, 2 - press for report, 3 - press for exit: "))
        if cls.actions == 1:
            return cls.actions
        elif cls.actions == 2:
            return cls.actions
        elif cls.actions == 3:
            print("You have existed: Try again ")
            return cls.action()
        else:
            print("Something went wrong, try again: ")
            return cls.action()

    @classmethod
    def download_input(cls):
        with open("data_saver.json") as data_file:
            cls.data = json.loads(data_file)
            for i in cls.data:
                print("activity", '-', i["activity"], ',', "weekday", '-', i["weekdays"], ',', "Money", '-', i["money"])


class Activity(Student):
    def input_activity(self):
        activity = input("\nPlease choose one of the activities: ")
        self.activity = super().set_up_json()
        while True:
            if activity in self.activity:
                return activity
            else:
                print("You have a wrong input, Try again: ")


class Weekday(Student):
    def input_weekdays(self):
        weekdays = input("\n Please enter one of the weekdays: ")
        self.weekdays = super().set_up_json()
        while True:
            if weekdays in self.weekdays:
                return weekdays
            else:
                print("You have a wrong input, try again: ")




def main():
    while True:
        Student.actions = Student.action()
        if Student.actions == 1:
            Student.student()
            # St = Student("Gor","ISotasd", "asd")
            Student.set_up_json()
            Student.info_input()
        elif Student.actions == 2:
            Student.download_input()
            return Student.action()
        elif Student.actions == 3:
            return Student.actions
        else:
            return Student.action()
main()

print("\n Thanks for using our program. ")















