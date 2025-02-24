# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
from datetime import datetime

class Note:
    HIGH: str = 'HIGH'
    MEDIUM: str = 'MEDIUM'
    LOW: str = 'LOW'

    def __init__(self, code: str, title: str, text: str, importance: str ):
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.creation_date = datetime.now()
        self.tags: list[str] = []

    def add_tag(self, tag: str):
        if tag  not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        return f'Date : {self.creation_date} \n {self.title}: {self.text} '


class Notebook:
    def __init__(self):
        self.notes: list[Note] = []

    def add_note(self, title:str, text:str, importance:str) -> int:
        new_code: int = len(self.notes) + 1

        for note in self.notes:
            if note.code == str(new_code)
                new_code += 1

        note = Note(str(new_code), title, text, importance)
        self.notes.append(note)
        return new_code

    def delete_note(self, code: int):
        for note in self.notes:
            if note.code == str(code):
                self.notes.remove(note)
                return

    def important_notes(self, importance) -> list[Note]:
        important_list: list[Note] = []
        for note in self.notes:
            if note.importance in [Note.HIGH, Note.MEDIUM]:
                important_list.append(note)
        return important_list

    def note_by_tag(self, tag : str) -> list[Note]:
        tag_list = []
        for note in self.notes:
            if tag in note.tags:
                tag_list.append(note)
        return tag_list

    def tag_with_most_notes(self) -> str:
        tags: list[str] = []
        for note in self.notes:
            tags.extend(note.tags)

