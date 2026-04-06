# Reception Guest Manager (Simplified)

guests = []


def get_name():
    while True:
        name = input("Enter name: ").strip().title()
        if name:
            return name
        print("Name cannot be empty.")
