# TODO: Agrega el código de las clases de la interfaz de usuario aquí. Borra este comentario al terminar.
from rich.console import Console
from rich.prompt import Prompt

from app.notebook import Notebook, Note


class NotebookConsole:
    def __init__(self, notebook: Notebook):
        self.notebook : Notebook = notebook
        self.console : Console = Console()

    def show_menu(self):
        self.console.print("Notebook")
        self.console.print("1. Add Notes")
        self.console.print("2. List Notes")
        self.console.print("3. Add tag to note")
        self.console.print("4. List important notes")
        self.console.print("5. Delete Note")
        self.console.print("6. Show notes by tag")
        self.console.print("7. Show tags with more notes")
        self.console.print("8. Exit")

        option: int = int(Prompt.ask("Select an option. ", choices = ["1", "2", "3", "4", "5", "6", "7", "8"]) )
        return option

    def add_note(self):
        self.console.print("[bold]Add note[/bold]")
        title : str = Prompt.ask("Title")
        text : str = Prompt.ask("Text")
        importance : str = Prompt.ask("Importance", choices=[Note.HIGH, Note.MEDIUM, Note.LOW])
        code : int = self.notebook.add_note(title, text, importance)
        self.console.print(f"Note added successfully with code {code}")

    def run(self):
        option: int = 0
        while option != 8:
            if option == 1:
                self.add_note()
            elif option == 2:
                self.list_notes()
                pass
            elif option == 2:
            elif option == 2:
            elif option == 2:
            elif option == 2:
            elif option == 2:
            elif option == 2:
