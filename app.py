contacts = {}
res = ""
choice = ""

def add():
    while(res != "X"):
        res = input("Enter your name: (X to exit)")
        contacts["name"] = res
        res = input("Enter your phone number: (X to exit)")
        contacts["phone"] = res

def delete():
    while(res != "X"):
        res = input("Delete by name: (X to exit)")
        contacts.pop(res)

def search():
    while(res != "X"):
        res = input("Search: (X to exit)")
        if res in contacts:
            print(f"{contacts[res]}")
if res == "A":
    add()
if res == "D":
    delete()
if res == "S":
    search()
if res == "P":
    pass
if res == "X":
    pass

if __name__ == "__main__":
    pass