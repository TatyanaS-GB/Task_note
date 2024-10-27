import json
import os
from datetime import datetime

# File to store the notes
NOTES_FILE = "notes.json"

# Load notes from the file
def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    return []

# Save notes to the file
def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

# Create a new note
def create_note(notes):
    title = input("Enter the title of the note: ")
    body = input("Enter the body of the note: ")
    timestamp = datetime.now().isoformat()
    note_id = len(notes) + 1
    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Note created successfully!")

# List all notes
def list_notes(notes):
    if not notes:
        print("No notes available.")
    else:
        for note in notes:
            print(f"ID: {note['id']}, Title: {note['title']}, Timestamp: {note['timestamp']}")

# Read a specific note
def read_note(notes):
    note_id = int(input("Enter the ID of the note to read: "))
    for note in notes:
        if note["id"] == note_id:
            print(f"Title: {note['title']}")
            print(f"Body: {note['body']}")
            print(f"Timestamp: {note['timestamp']}")
            return
    print("Note not found.")

# Edit a specific note
def edit_note(notes):
    note_id = int(input("Enter the ID of the note to edit: "))
    for note in notes:
        if note["id"] == note_id:
            note["title"] = input("Enter the new title: ")
            note["body"] = input("Enter the new body: ")
            note["timestamp"] = datetime.now().isoformat()
            save_notes(notes)
            print("Note edited successfully!")
            return
    print("Note not found.")

# Delete a specific note
def delete_note(notes):
    note_id = int(input("Enter the ID of the note to delete: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Note deleted successfully!")
            return
    print("Note not found.")