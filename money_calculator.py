import json

class User:
    def __init__(self, name):
        self.name = name
        self.spendings = []

    def addSpending(self, activityType, dayOfWeek, amount):
        newSpending = {}
        newSpending["activity"] = activityType
        newSpending["day"] = dayOfWeek
        newSpending["amount"] = amount
        self.spendings.append(newSpending)

    def printSpendings(self):
        print(self.spendings)

def main():

    userName = input("Please let us know your Name")
    user = User(userName)
    
    while True:
        choice = input("Do you want to add Spending? please type Yes/No")
        if (choice == "No"):
            user.printSpendings()
            print("Thanks for using our App")
            break
        else: 
            activity = input("Please type the activity")
            day = input("Please type the day of the week  ")
            amount = input("Please type the amount ")
            
            user.addSpending(activity, day, amount)

main()









