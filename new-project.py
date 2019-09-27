import json
print("\n Welcome to MoneySaver program")
print("\n Please enter your option")


class Student:
    new_data = {}

    def __init__(self):
        pass

    @staticmethod
    def student_info():
        user = {}
        user['name'] = str(input("Please enter your name: "))
        user['password'] = str(input("Please enter the password: "))
        user['data'] = []
        with open('data_saver', 'w') as file:
            file.write(json.dumps(user))

    @staticmethod
    def set_up_json():
        with open("main.json") as data_file:
            file = json.load(data_file)
            activity = file['student']['activity']
            weekdays = file['student']['weekdays']
            money = file['student']['budget']
            return weekdays, activity, money

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
        for i in cls.set_up_json():
            print(i)
        Student.new_data['activity'] = Activity.input_activity()
        for j in cls.set_up_json():
            print(j)
        Student.new_data['weekday'] = Weekday.input_weekdays()
        for k in cls.set_up_json():
            print(k)
        Student.new_data['budget'] = Student.input_money()
        with open('data_saver', 'r') as data_file:
            data = json.loads(data_file)
            data['data'].append(Student.new_data)
        with open('data_saver', 'w') as file:
            file.write(json.dumps(data))

    @classmethod
    def action(cls):
        cls.actions = int(input("\n1 - press for adding, 2 - press for report, 3 - press for exit: "))
        if cls.actions == 1:
            return cls.actions
        elif cls.actions == 2:
            return cls.action
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
    @staticmethod
    def input_activity():
        term = input("\nPlease select one of this activities: ")
        while True:
            if term in Student.set_up_json():
                return term
            else:
                term = input("\nYou have typed something wrong, input it again: ")


class Weekday(Student):
    @staticmethod
    def input_weekdays():
        weekday = input("\nPlease select one of the weekdays: ")
        while True:
            if weekday in Student.set_up_json():
                return weekday
            else:
                weekday = input("\nYou have typed something wrong, input it again: ")





def main():
    while True:
        actions = Student.action()
        if actions == 1:
            Student.student_info()
            Student.set_up_json()
            Student.info_input()
            Student.input_money()
        elif actions == 2:
            Student.download_input()
        elif actions == 3:
            return actions
        else:
            return Student.action()


main()

print("\n Thanks for using our program. ")








