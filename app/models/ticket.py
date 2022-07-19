import random
from pydantic import BaseModel, Field


type = ('Issue', 'Bug', 'Task')
ID_CHARACTERS = 'ABCDEFGHJKLMNPQRSTUVWXYZ'


class Ticket(BaseModel):
    type: str = Field("Type", max_length=10)
    title: str = Field("Title", max_length=255)
    description: str = Field("Description")
    category: str = Field("Description")


class Issue(object):
    title: str = Field("Title", max_length=255)
    description: str = Field("Description", max_length=255)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    @classmethod
    def create_from_ticket(cls, ticket: Ticket):
        return cls(ticket.title, ticket.description)



class Bug(Issue):
    label: str

    @staticmethod
    def generate_title():
        word = "".join(random.choices(ID_CHARACTERS, k=3))
        number = random.randint(1,1000)
        return f"bug-{word}-{number}"

    @classmethod
    def create_from_ticket(cls, ticket: Ticket):
        return cls(Bug.generate_title(), ticket.description )


class Task():
    title: str = Field("Title", max_length=255)
    category: str = Field("Category")

    def __init__(self, title, category):
        self.title = title
        self.category = category

    @classmethod
    def create_from_ticket(cls, ticket: Ticket):
        return cls(ticket.title, ticket.category)

