import json


class User:
    print("\nWelcome to MoneySaver program")

    file = "main.json"

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

    def set_up_json(self, file, activities, weekdays):
        self.activities = activities
        self.weekdays = weekdays
        with open(file) as data_file:
            file = json.loads(data_file)
            self.activities = file['student']['activity']
            self.weekdays = file['student']['weekdays']
            return self.activities, self.weekdays


def action():
    print("\nPlease select one of these actions: ")
    actions = int(input("1–press for adding, 2–for the report, 3–exist "))
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
        key = input("Please choose one of the activities: ")
        if key in self.activities:
            return key
        else:
            print("You have a wrong input, please type again:")
            return Activity







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
            activity = Activity
            activity.choose_activity(activity)
            day = input("Please type the day of the week: ")
            amount = input("Please type the amount: ")

            user.add_spending(activity, day, amount)


main()
