# Contact manager application

contacts = []

def add_contact():
    name = input("Enter contact name: ")
    
    if any(contact[0].lower() == name.lower() for contact in contacts):
        print("Contact name already exists.\n")
        return
    
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    
    contacts.append((name, phone, email))
    print("Contact added successfully.\n")

def view_contact():
    if not contacts:
        print('contacts not found.')
    else:
        print('\nContacts list:')
        for contact in contacts:
            print(f'Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}')
    print()

def search_contact():
    name = input("Enter the name to search: ")
    found = False
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print(f"Found contact: Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
            found = True
            break
    if not found:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    found = False
    for i, contact in enumerate(contacts):
        if contact[0].lower() == name.lower():
            new_phone = input("Enter new phone number: ")
            contacts[i] = (contact[0], new_phone, contact[2]) 
            print(f"Contact updated: Name: {contact[0]}, Phone: {new_phone}, Email: {contact[2]}\n")
            found = True
            break
    if not found:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    found = False
    for i, contact in enumerate(contacts):
        if contact[0].lower() == name.lower():
            del contacts[i]
            print(f"Contact {name} deleted successfully.\n")
            found = True
            break
    if not found:
        print("Contact not found.\n")

def menu():
    while True:
        print("Contact Manager Menu:")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Search contacts by name")
        print("4. Update contact's phone number")
        print("5. Delete contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.\n")

menu()

