# TODO: Agrega el código necesario para que la aplicación pueda ser ejecutada. Borra este comentario al terminar.
from app.console import NotebookConsole
from app.notebook import Notebook
def main():
    notebook: Notebook = Notebook()
    console: NotebookConsole = NotebookConsole(notebook)
    console.run()


if __name__ == "__main__":
    main()

