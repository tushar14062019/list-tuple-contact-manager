# Case Study: Contact Manager Application Using List and Tuple

## Objective

The objective of this case study is to design and implement a simple Contact Manager application using Python's list and tuple data structures. The application should allow users to store, retrieve, update, and delete contacts efficiently while ensuring data integrity.

By the end of this case study, learners will be able to:

- Understand the use of list and tuple for data storage.
- Implement basic CRUD (Create, Read, Update, Delete) operations using Python.
- Develop modular code using functions.
- Apply logical thinking for managing contacts effectively.

## Case Study Scenario

A small business owner wants a simple console-based contact manager to store customer and supplier details. The contact information includes name, phone number, and email. Since names and emails remain unchanged once added, they are stored in tuples, while the contact list itself is stored as a list to allow modifications.
The business owner requires the following functionalities:

- Add a new contact
- View all contacts
- Search for a contact by name
- Update a contact's phone number
- Delete a contact

## Tasks

### Task 1: Data Structure Design

Use a list to store multiple contacts.
Each contact is stored as a tuple containing:
```
  Name (String)
  Phone Number (String)
  Email (String)
```

### Task 2: Implementing CRUD Operations

1. Add a New Contact

    Prompt the user for name, phone number, and email.
    Append the contact as a tuple to the list.
    Prevent duplicate names.

2. View All Contacts

    Display all stored contacts in a formatted manner.

3. Search for a Contact by Name

    Allow the user to enter a name.
    Find and display the corresponding contact.

4. Update a Contact’s Phone Number

    Search for a contact by name.
    If found, modify the phone number while keeping the name and email unchanged.
    Since tuples are immutable, replace the entire tuple in the list.

5. Delete a Contact

    Search for a contact by name.
    Remove the contact from the list
   
### Task 3: Code Implementation

Implement the above functionalities using functions and a menu-driven approach.

## Sample output

```markdown
Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 1

Enter Name: Alice Johnson
Enter Phone Number: 9876543210
Enter Email: alice@example.com
Contact added successfully!

-------------------------------------------------

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 1

Enter Name: Bob Smith
Enter Phone Number: 9123456789
Enter Email: bob@example.com
Contact added successfully!

-------------------------------------------------

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 2

List of Contacts:
1. Alice Johnson - 9876543210 - alice@example.com
2. Bob Smith - 9123456789 - bob@example.com

-------------------------------------------------

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 3

Enter name to search: Alice Johnson
Contact Found: Alice Johnson - 9876543210 - alice@example.com

-------------------------------------------------

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 4

Enter name to update: Bob Smith
Enter new phone number: 9988776655
Contact updated successfully!

-------------------------------------------------

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 5

Enter name to delete: Alice Johnson
Contact deleted successfully!

-------------------------------------------------

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 2

List of Contacts:
1. Bob Smith - 9988776655 - bob@example.com

-------------------------------------------------

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 6

Exiting Contact Manager. Goodbye!

```
Each operation should perform the expected modifications and display appropriate messages.
