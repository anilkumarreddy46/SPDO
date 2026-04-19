# Smart Personal Data Organizer (SPDO)

#--------- Data Storage ------------------
contacts = []
notes = []
tasks = []

# ------------------ Contact Module ------------------
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)

    print("Contact added successfully!")

def view_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for c in contacts:
            print("Name:", c["name"], "| Phone:", c["phone"], "| Email:", c["email"])

# ------------------ Notes Module ------------------
def add_note():
    note = input("Enter your note: ")
    notes.append(note)
    print("Note saved successfully!")

def view_notes():
    if len(notes) == 0:
        print("No notes available.")
    else:
        print("\nNotes:")
        for n in notes:
            print("-", n)

# ------------------ Task Module ------------------
def add_task():
    task_name = input("Enter task: ")
    deadline = input("Enter deadline: ")

    task_data = {"task": task_name, "deadline": deadline}
    tasks.append(task_data)

    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nTask List:")
        for t in tasks:
            print("Task:", t["task"], "| Deadline:", t["deadline"])

# ------------------ Search Module ------------------
def search_contact():
    name = input("Enter contact name to search: ").lower()
    found = False

    for c in contacts:
        if c["name"].lower() == name:
            print("Contact Found!")
            print("Name:", c["name"])
            print("Phone:", c["phone"])
            print("Email:", c["email"])
            found = True

    if not found:
        print("Contact not found.")

# ------------------ Main Menu ------------------
def main():
    while True:
        print("\n------ Smart Personal Data Organizer ------")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Add Note")
        print("4. View Notes")
        print("5. Add Task")
        print("6. View Tasks")
        print("7. Search Contact")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            add_note()
        elif choice == 4:
            view_notes()
        elif choice == 5:
            add_task()
        elif choice == 6:
            view_tasks()
        elif choice == 7:
            search_contact()
        elif choice == 8:
            print("Thank you for using SPDO!")
            break
        else:
            print("Invalid choice, try again.")

# Run program
main()