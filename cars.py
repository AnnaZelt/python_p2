#imports
from enum import Enum
import csv
import os

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

# Initializing global variables
cars = []
found_car = []
#Constant header"
header = ["COLOR","MODEL","TYPE"]
csv_file_path = "cars.csv"

#Clear the CLI
def clean():
    os.system('cls')

#Save to csv file
def save(csv_file_path):
    global cars, header
    # Open the CSV file in write mode
    with open(csv_file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        if header:
            csv_writer.writerow(header)  # Write the header row only if it exists

        csv_writer.writerows(cars)  # Write the data rows

# #Load from a csv file
def load():
    global cars, csv_file_path, header
    cars = []  # Reset the cars list before loading

    # Read data from the CSV file
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader, None)  # Read the header row or None if empty

        for row in csv_reader:
            cars.append(row)  # Append the remaining rows

# def load():
#     global cars, csv_file_path, header
#     # Read data from the CSV file
#     with open(csv_file_path, mode='r') as csv_file:
#         # Create a CSV reader object
#         csv_reader = csv.reader(csv_file)
#         # Skip the header row if needed
#         header = next(csv_reader)
        
#         # Read the remaining rows
#         for row in csv_reader:
#             cars.append(row)
#     return cars

#Liniks the selection ENUMs to the menu() method
def displayMenu():
    for x in Actions: printPink(f"{x.value} - {x.name}")
    return Actions(int(input("Select an action: ")))

#The action selection menu method
def menu():
    while(True):
        menuSelection = displayMenu()
        if menuSelection == Actions.PRINT and cars !=[]: 
            print(cars)
        else: printPink("No items to show.")
        if menuSelection == Actions.ADD: 
            add()
        #Saves data to the csv file, cleans the CLI and ends menu()
        if menuSelection == Actions.EXIT:
            save(csv_file_path)
            clean()
            return
        if menuSelection == Actions.SEARCH:
            search()
        if menuSelection == Actions.DELETE:
            remove()
        if menuSelection == Actions.UPDATE:
            update()

#Change an item with search()
def update():
    global cars
    printPink("Choose an item to update: ")
    searchTerm = input("Search by color: ")
    for row in cars:
        if row[Fields.COLOR.value] == searchTerm:
            row[Fields.COLOR.value] = input("Enter the new color: ")
            row[Fields.TYPE.value] = input("Enter the new type: ")
            row[Fields.MODEL.value] = input("Enter the new model: ")
            printPink("Car updated.")
            return

# def update():
#     global cars, found_car
#     found_car = []
#     printPink("Choose an item to update: ")
#     searchTerm = input("Search by color: ")
#     for row in cars:
#         for column in range(0,1): 
#             if row[column] == searchTerm:
#                 row[0] = input("Enter the new color: ")
#                 row[1] = input("Enter the new type: ")
#                 row[2] = input("Enter the new model: ")
#                 printPink(f"Changed: {found_car}")
#                 return
   
#Remove an item with search()
def remove():
    global cars
    printPink("Choose an item to delete: ")
    choice = search()
    printPink(f"removed: {choice}")
    cars.remove(choice)

#Add an item
def add():
    cars.append({
            input('Enter color: '), 
            input('Enter model: '),
            input('Enter type: ')
            })

#Search for an item by color       
def search():
    global cars, found_car
    isFound = False
    found_car = []
    searchTerm = input("Search by color: ")
    for row in cars:
        for column in range(0,1):
            if row[column] == searchTerm:
                isFound = True
                found_car = row
    if isFound:
        printPink(f"Found: {found_car}")
        return found_car
    else: printPink("No item found.")

def printPink(skk): print("\033[95m {}\033[00m" .format(skk))

#start and end point - it loads the csv file with the start
if __name__ == "__main__":
    load()
    menu()
