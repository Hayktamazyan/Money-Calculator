import json


class User:
    print("\nWelcome to MoneySaver program")

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.spendings = []

    def add_spending(self, activityType, dayOfWeek, amount):
        newSpending = {}
        newSpending["activity"] = activityType
        newSpending["day"] = dayOfWeek
        newSpending["amount"] = amount
        self.spendings.append(newSpending)

    def print_spendings(self):
        print(self.spendings)

    def set_up_json(self):
        with open("main.json") as data_file:
            file = json.load(data_file)
            self.activities = file['student']['activity']
            self.weekdays = file['student']['weekdays']
            return self.activities, self.weekdays

    @classmethod
    def upload_new_data(cls):
        with open('main.json', 'r') as file:
            data = json.load(file)
            data['newSpending'].append(cls.spendings)
        with open('main.json', 'w') as file:
            file.write(json.dumps(data))
        pass


def choose_action():
    print("\nPlease select one of these actions: ")
    actions = int(input("\n1 - press for adding, 2 - press for report, 3 - press for exit: "))
    if actions == 1 or actions == 2:
        return actions
    elif actions == 3:
        print("\nYou have exited")
        return actions
    else:
        print("\nSomething went wrong, try again: ")
        return choose_action()


class Activity(User):
    def choose_activity(self):
        print("\nHere are the activities: ")
        for i in self.activities:
            print(i)
        key = input("\nPlease choose one of the activities: ")
        if key in self.activities:
            print("\nYou chose " + key + ":")
            return key
        else:
            print("\nYou have a wrong input, please type again:")
            return Activity.choose_activity(self)


class Weekday(User):
    def choose_weekday(self):
        print("\nHere are the weekdays: ")
        for i in self.weekdays:
            print(i)
        day = input("\nPlease choose one of the weekdays: ")
        if day in self.weekdays:
            print("\nYou chose " + day + ":")
            return day
        else:
            print("\nYou have a wrong input, please try again: ")
            return Weekday.choose_weekday(self)


class Budget(User):
    def input_money(self):
        while True:
            data = input("\nPlease enter the amount of money: ")
            temp = data.replace('.', '', 1)
            if temp.isdigit():
                data = float(data)
                return data
            else:
                print("\nSomething went wrong, try again:")
                return Budget.input_money(self)


def main():
    action = choose_action()
    while True:
        if action == 1:
            username = input("\nPlease let us know your Name: ")
            userpassword = input("\nPlease enter your Password: ")
            user = User(username, userpassword)
            choice = input("Do you want to add Spending? please type Yes/No")
            if choice == "No":
                user.print_spendings()
                print("Thanks for using our App")
                break
            else:
                activity = Activity("name", "password")
                activity.set_up_json()
                activity.choose_activity()
                weekdays = Weekday("name", "password")
                weekdays.set_up_json()
                weekdays.choose_weekday()
                money = Budget("name", "password")
                money.input_money()
                user.add_spending(activity, weekdays, money)
                user.print_spendings()
                User.upload_new_data()
                break
        elif action == 2:
            User.upload_new_data()
            pass
        else:
            action == 3
            print("\nThanks for using our program")
            break


main()


