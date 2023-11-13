journal ={}

def create_note():
    note_id = input("please enter note id")
    note_content=input('please ernter the note')
    journal[note_id] = note_content
    print(f"note {note_id} created")

def list_notes():
    if not journal:
        print('no notes in the journal')
    else:
        for note_id,note_content in journal.items():
            print(f"{note_id}: {note_content[:15]}")

def retrive_note():
    note_id = input("please enter the id of the note you want retrived")
    for note_id,note_content in journal.items():
        print(f"Note {note_id}:{note_content} ")
    if not journal:
        print("no notes with that id found")

def delete_note():
    note_id = input("please enter the id of the note you want to delete")
    for note_id,note_content in journal.items():
        del  [note_id]
        print(f"{note_id} deleted from journal")
    if not  journal:
        print("no such note exists in the journal")

def search_note():
    keyword = input("please enter the word you want to find")
    found = []
    for note_id, note_content in journal.items():
        if keyword in note_content:
            found.append((note_id, note_content))
    if found:
        print(f"Notes containing '{keyword}':")
        for note_id, note_content in found:
            print(f"{note_id}: {note_content[:20]}...")
    else:
        print(f"No notes containing '{keyword}' found.")

while True:
    print("Welcome \nto add a note press 1\nto remove list all notes press 2\n"
          "to retrive a note press 3\nto delete a note press 4\nto search in notes press 5\n"
          "to quit 6")

    choice = input('please choose the desired operation: ')

    if choice == '1':
        create_note()
    if choice == '2':
        list_notes()
    if choice == '3':
        retrive_note()
    if choice == '4':
        delete_note()
    if choice == '5':
        search_note()
    if choice == '6':
        print("quitting")