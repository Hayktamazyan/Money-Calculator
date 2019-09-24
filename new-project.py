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

    def __init__(self, name, password, data):
        self.name = name
        self.password = password
        self.data = data
        Student.user['name'] = str(input("\nPlease enter your name: "))
        Student.user['password'] = str(input("\nPlease enter your password: "))
        Student.new_data[data] = self
        
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
        cls.data = super().set_up_json()
        for j in cls.data['activity']:
            print(j)
        Student.new_data = Activity.input_activity()
        for i in cls.data['weekdays']:
            print(i)
        Student.new_data = Weekday.input_weekdays()
        for a in cls.data['money']:
            print(a)
        Student.new_data = Student.input_money()
        with open('data_saver.json', 'r') as file:
            cls.data = json.load(file)
        with open('data_saver.json', 'w') as f:
            f.write(json.dumps(cls.data))


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
   pass
main()

print("\n Thanks for using our program. ")



















