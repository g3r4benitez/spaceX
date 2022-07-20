import random
from typing import Optional
from pydantic import BaseModel, Field


type = ('Issue', 'Bug', 'Task')
ID_CHARACTERS = 'ABCDEFGHJKLMNPQRSTUVWXYZ'


class Ticket(BaseModel):
    type: Optional[str] = Field(max_length=10)
    title: Optional[str] = Field(max_length=255)
    description: Optional[str] = Field()
    category: Optional[str] = Field()


class BaseTask(object):
    _title: str
    id: str

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title_value):
        if title_value and len(title_value):
            self._title = title_value
        else:
            raise ValueError("title: 'title' is required")


class Issue(BaseTask):
    _description: str

    def __init__(self, title, description):
        self.title = title
        self.description = description

    @classmethod
    def create_from_ticket(cls, ticket: Ticket):
        return cls(ticket.title, ticket.description)

    @property
    def descripton(self):
        return self._description

    @descripton.setter
    def description(self, description_value):
        if description_value and len(description_value):
            self._description = description_value
        else:
            raise ValueError("description: 'description' is required")


class Bug(Issue):

    @staticmethod
    def generate_title():
        word = "".join(random.choices(ID_CHARACTERS, k=3))
        number = random.randint(1,1000)
        return f"bug-{word}-{number}"

    @classmethod
    def create_from_ticket(cls, ticket: Ticket):
        return cls(Bug.generate_title(), ticket.description )

    def __str__(self):
        return {
            "title": self.title,
            "description": self.description
        }


class Task(BaseTask):
    _category: str

    def __init__(self, title, category):
        self.title = title
        self.category = category

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category_value):
        if category_value in ("Maintenance", "Research", "Test"):
            self._category = category_value
        else:
            raise ValueError("category: category should be one of these options: Maintenance, Research, Test")

    @classmethod
    def create_from_ticket(cls, ticket: Ticket):
        return cls(ticket.title, ticket.category)

