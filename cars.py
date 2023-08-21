#imports
from enum import Enum
import csv

#enums
class Actions(Enum):
    PRINT = 0
    ADD = 1
    UPDATE = 2
    DELETE = 3
    SEARCH = 4
    EXIT = 5

class Fields(Enum):
    COLOR = 0
    MODEL = 1
    TYPE = 2

cars = []

def save():
    # Open the CSV file in write mode
    with open(csv_file_path, mode='w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)
        # Write the data to the CSV file
        csv_writer.writerows(cars)

csv_file_path = "cars.csv"

def load(csv_file_path):
    global cars
    # Read data from the CSV file
    with open(csv_file_path, mode='r') as csv_file:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)
        
        # Skip the header row if needed
        header = next(csv_reader)
        
        # Read the remaining rows
        for row in csv_reader:
            cars.append(row)
    return cars

def displayMenu():
    for x in Actions: print(f"{x.value} - {x.name}")
    return Actions(int(input("Select an action: ")))

def menu():
    while(True):
        menuSelection = displayMenu()
        if menuSelection == Actions.PRINT: print(cars)
        if menuSelection == Actions.ADD: 
            add()
        if menuSelection == Actions.EXIT: 
            return
        if menuSelection == Actions.SEARCH:
            search()

def add():
    cars.append({
            Fields.COLOR.name:input('Enter color: '), 
            Fields.MODEL.name:input('Enter model: '),
            Fields.TYPE.name:input('Enter type: ')
            })
        
def search():
    global cars
    found = False
    found_car = ""
    target = input("Search by color: ")
    for row in cars:
        print(row)
        if row == target:
            found = True
            found_car = target
        if found:
            return found_car
    print("-----------------")
    print(found_car)

if __name__ == "__main__":
    load(csv_file_path)
    menu()