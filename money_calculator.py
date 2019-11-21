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


def action():
    print("\nPlease select one of these actions: ")
    actions = int(input("1–press for adding, 2–for the report, 3–exist: "))
    if actions == 1 or actions == 2:
        return actions
    elif actions == 3:
        print("You have exited ")
        return actions
    else:
        print("You have wrong input try again: ")
        return actions


class Activity(User):
    def choose_activity(self):
        print("\nHere are the activities: "
              "supermarket, " + "cafeteria")
        key = input("\nPlease choose one of the activities: ")
        if key in self.activities:
            print("\nYou chose " + key + ":")
            return key
        else:
            print("\nYou have a wrong input, please type again:")
            return Activity.choose_activity(self)


class Weekday(User):
    def choose_weekday(self):
        print("\nHere are the weekdays: "
              "monday, " + "tuesday, " + "wednesday, " + "thursday, " + "friday, " + "saturday, " + "sunday")
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







def main():
    action()
    username = input("\nPlease let us know your Name: ")
    userpassword = input("\nPlease enter your Password: ")
    user = User(username, userpassword)

    while True:
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
            # day = input("Please type the day of the week: ")
            # amount = input("Please type the amount: ")

            # user.add_spending(activity, day, amount)


main()
