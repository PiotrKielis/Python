import datetime


class Note:
    id_counter = 0

    def __init__(self, text, tag):
        self.text = text
        self.tag = tag
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Note.id_counter += 1
        self.ID = Note.id_counter

    def match(self, keyword):
        return keyword in self.text or keyword in self.tag


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, text, tag):
        self.notes.append(Note(text, tag))

    def modify_text(self, note_id, new_text):
        for note in self.notes:
            if note.ID == note_id:
                note.text = new_text
                break

    def modify_tag(self, note_id, new_tag):
        for note in self.notes:
            if note.ID == note_id:
                note.tag = new_tag
                break

    def search(self, keyword):
        return [note for note in self.notes if note.match(keyword)]


class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.options = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit,
        }

    def show_menu(self):
        print(
            """
Notebook Menu
1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit"""
        )

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter an option: ")
            action = self.options.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}\n".format(note.ID, note.tag, note.text))

    def search_notes(self):
        keyword = input("Enter a keyword to search for: ")
        notes = self.notebook.search(keyword)
        self.show_notes(notes)

    def add_note(self):
        text = input("Enter a note: ")
        tag = input("Enter a tag: ")
        self.notebook.new_note(text, tag)
        print("Note added successfully")

    def modify_note(self):
        note_id = int(input("Enter a note ID to modify: "))
        note = self.find_note_by_id(note_id)
        if note:
            print("1. Modify text")
            print("2. Modify tag")
            choice = input("Enter an option: ")
            if choice == "1":
                new_text = input("Enter new text: ")
                self.notebook.modify_text(note_id, new_text)
                print("Text modified successfully")
            elif choice == "2":
                new_tag = input("Enter new tag: ")
                self.notebook.modify_tag(note_id, new_tag)
                print("Tag modified successfully")
            else:
                print("{0} is not a valid choice".format(choice))
        else:
            print("Note not found")

    def find_note_by_id(self, note_id):
        for note in self.notebook.notes:
            if note.ID == note_id:
                return note
        return None

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
