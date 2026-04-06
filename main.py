# Reception Guest Manager (Simplified)

guests = []


def get_name():
    while True:
        name = input("Enter name: ").strip().title()
        if name:
            return name
        print("Name cannot be empty.")

def add_guest():
    name = get_name()
    if name in guests:
        print("Name already exists.")
    else:
        guests.append(name)
        print(name, "added.")
