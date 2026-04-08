# Reception Guest Manager

# List to store guest names
guests = []


# Function to safely get a name
def get_name():
    while True:
        # Get input, remove spaces, and capitalize properly
        name = input("Enter name: ").strip().title()

        # Validation: make sure it's not empty
        if name:
            return name
        print("Name cannot be empty.")


# Function to add a guest
def add_guest():
    name = get_name()

    # Prevent duplicates
    if name in guests:
        print("Name already exists.")
    else:
        guests.append(name)
        print(name, "added.")


# Function to modify an existing guest
def modify_guest():
    old_name = get_name()

    # Check if guest exists
    if old_name in guests:
        print("Enter new name:")
        new_name = get_name()

        # Check for duplicate new name
        if new_name in guests:
            print("That name already exists.")
        else:
            # Replace old name with new one
            index = guests.index(old_name)
            guests[index] = new_name
            print(old_name, "changed to", new_name)
    else:
        print("Guest not found.")


# Function to remove a guest
def remove_guest():
    name = get_name()

    if name in guests:
        guests.remove(name)
        print(name, "removed.")
    else:
        print("Guest not found.")


# Function to sort guests alphabetically
def sort_guests():
    guests.sort()
    print("Guests sorted.")


# Function to show total guests
def show_count():
    print("Total guests:", len(guests))


# Function to print invitations
def show_invitations():
    if not guests:
        print("No guests.")
        return

    for guest in guests:
        print(f"Dear {guest}, you are invited!")


# Main menu function
def main():
    while True:
        print("\n1 Add")
        print("2 Modify")
        print("3 Remove")
        print("4 Sort")
        print("5 Count")
        print("6 Invitations")
        print("0 Exit")

        choice = input("Choice: ")

        if choice == "1":
            add_guest()
        elif choice == "2":
            modify_guest()
        elif choice == "3":
            remove_guest()
        elif choice == "4":
            sort_guests()
        elif choice == "5":
            show_count()
        elif choice == "6":
            show_invitations()
        elif choice == "0":
            break
        else:
            print("Invalid option. Try again.")


# Run the program
main()