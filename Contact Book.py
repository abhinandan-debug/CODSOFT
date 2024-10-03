# Initialize an empty dictionary for storing contacts
contact_book = {}

# Function to add a new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact_book[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print(f"Contact for {name} added successfully!")

# Function to view all contacts
def view_contacts():
    if not contact_book:
        print("No contacts found.")
    else:
        for name, details in contact_book.items():
            print(f"\nName: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")

# Function to search for a contact by name
def search_contact():
    name = input("Enter Name to search: ")
    if name in contact_book:
        details = contact_book[name]
        print(f"\nName: {name}")
        print(f"Phone: {details['Phone']}")
        print(f"Email: {details['Email']}")
        print(f"Address: {details['Address']}")
    else:
        print(f"No contact found for {name}.")

# Function to update a contact
def update_contact():
    name = input("Enter Name of the contact to update: ")
    if name in contact_book:
        phone = input("Enter new Phone Number: ")
        email = input("Enter new Email: ")
        address = input("Enter new Address: ")
        
        contact_book[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        print(f"Contact for {name} updated successfully!")
    else:
        print(f"No contact found for {name}.")

# Function to delete a contact
def delete_contact():
    name = input("Enter Name of the contact to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact for {name} deleted successfully!")
    else:
        print(f"No contact found for {name}.")

# Menu-driven interface
def contact_book_menu():
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the contact book menu
if __name__ == "__main__":
    contact_book_menu()
