import json


class User:
    print("\nWelcome to MoneySaver program")
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.spendings = []

    def addSpending(self, activityType, dayOfWeek, amount):
        newSpending = {}
        newSpending["activity"] = activityType
        newSpending["day"] = dayOfWeek
        newSpending["amount"] = amount
        self.spendings.append(newSpending)

    def printSpendings(self):
        print(self.spendings)

    @staticmethod
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

    @classmethod
    def set_up_json(cls):
        with open("main.json") as data_file:
            file = json.loads(data_file)
            cls.activity = file['student']['activity']
            cls.weekdays = file['student']['weekdays']


class Activity(User):
    def use_activity(self):
        key = input("Please choose one of the activities: ")
        while self.activity:
            if key in self.activity:
                return key
            else:
                print("You type something wrong, Try again ")
                return key





def main():
    User.action()
    userName = input("\nPlease let us know your Name: ")
    userPassword = input("\nPlease enter your Password: ")
    user = User(userName, userPassword)

    while True:
        choice = input("Do you want to add Spending? please type Yes/No")
        if choice == "No":
            user.printSpendings()
            print("Thanks for using our App")
            break
        else:
            activity = Activity.use_activity()
            day = input("Please type the day of the week: ")
            amount = input("Please type the amount: ")

            user.addSpending(activity, day, amount)


main()
