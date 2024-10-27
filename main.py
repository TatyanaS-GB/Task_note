import note

def main():
    notes = note.load_notes()

    while True:
        print("\nNote-taking Application")
        print("1. Create a new note")
        print("2. List all notes")
        print("3. Read a note")
        print("4. Edit a note")
        print("5. Delete a note")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            note.create_note(notes)
        elif choice == "2":
            note.list_notes(notes)
        elif choice == "3":
            note.read_note(notes)
        elif choice == "4":
            note.edit_note(notes)
        elif choice == "5":
            note.delete_note(notes)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()