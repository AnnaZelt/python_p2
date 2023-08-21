from enum import Enum
import json
import os

contacts = []

class Actions(Enum):
    PRINT = 0
    ADD = 1
    UPDATE = 2
    DELETE = 3
    SEARCH = 4
    EXIT = 5

def save():
    with open("contacts.json", "w") as saveFile:
        json.dump(contacts, saveFile)

def load():
    global contacts
    if os.path.exists('contacts.json') and os.path.getsize('contacts.json') > 0:
        with open('contacts.json', 'r') as saveFile:
            contacts = json.load(saveFile)
    else:
        contacts = []
    
def displayMenu():
    for x in Actions: print(f"{x.value} - {x.name}")
    return Actions(int(input("Select an action: ")))

def menu():
    while(True):
        res = displayMenu()
        if res == Actions.PRINT: print(contacts)
        if res == Actions.ADD: contacts.append({"name":input('Enter name: '), "Phone":input('Enter phone number: ')})
        if res == Actions.EXIT: 
            save()
            return
        if res == Actions.UPDATE: 
            search()
            update()
        if res == Actions.DELETE:
            search()
            remove()
        if res == Actions.SEARCH:
            search()

def update():
    # global contacts
    # print("Select contact to update: ")
    # found_contact = search()
    # contacts.update =({"name":input('Enter new name: '), "Phone":input('Enter new phone number: ')})
    pass


def remove():
    global contacts
    print("Select contact to remove: ")
    found_contact = search()
    contacts.remove(found_contact)

def search():
    global contacts
    found = False
    found_contact = ""
    target = input("Search by name: ")
    for contact in contacts:
        if contact["name"] == target:
            found = True
            found_contact = target
        if found:
            return found_contact
        
if __name__ == "__main__":
    load()
    menu()
