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

def remove_guest():
    name = get_name()
    if name in guests:
        guests.remove(name)
        print(name, "removed.")
    else:
        print("Guest not found.")


def sort_guests():
    guests.sort()
    print("Guests sorted.")

def show_count():
    print("Total guests:", len(guests))


def show_invitations():
    if not guests:
        print("No guests.")
        return

    for guest in guests:
        print(f"Dear {guest}, you are invited!")

