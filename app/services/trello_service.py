import random

import requests
from app.core.config import (TRELLO_KEY, TRELLO_TOKEN, TRELLO_BOARD, TRELLO_URL, TRELLO_LIST_TODO, TRELLO_LABEL_BUG,
TRELLO_LIST_GENERIC, TRELLO_LABEL_MAINTENANCE, TRELLO_LABEL_RESEARCH, TRELLO_LABEL_TEST)
from app.models.ticket import Bug, Issue, Task

LABELS = {
    'Maintenance': TRELLO_LABEL_MAINTENANCE,
    'Research': TRELLO_LABEL_RESEARCH,
    'Test': TRELLO_LABEL_TEST
}

class TrelloService:

    def __init__(self, ):
        self.url_base = TRELLO_URL

    def get_board(self):
        r = requests.get(f"{self.url_base}/boards/{TRELLO_BOARD}", data={
            'key': TRELLO_KEY,
            'token': TRELLO_TOKEN
        })
        return r.json()

    def create_card(self, name: str, desc: str ):
        r = requests.post(
            f"{self.url_base}/cards?key={TRELLO_KEY}&token={TRELLO_TOKEN}&idBoard={TRELLO_BOARD}",
            data={
                'name': name,
                'desc': desc,
                'idList': "5092e91c5373eeaf050071f8",
                'idBoard': TRELLO_BOARD
            },

        )
        return r.status_code

    def create_issue(self, issue: Issue):
        r = requests.post(
            f"{self.url_base}/cards?key={TRELLO_KEY}&token={TRELLO_TOKEN}&idBoard={TRELLO_BOARD}",
            data={
                'name': issue.title,
                'desc': issue.description,
                'idList': TRELLO_LIST_TODO,
                'idBoard': TRELLO_BOARD
            },

        )
        return r.status_code

    def create_bug(self, bug: Bug):
        r = requests.post(
            f"{self.url_base}/cards?key={TRELLO_KEY}&token={TRELLO_TOKEN}&idBoard={TRELLO_BOARD}",
            data={
                'name': bug.title,
                'desc': bug.description,
                'idList': TRELLO_LIST_GENERIC,
                'idBoard': TRELLO_BOARD,
                'idLabels': [TRELLO_LABEL_BUG,],
                'idMembers': [self.get_random_member(),]
            },

        )
        return r.status_code

    def create_task(self, task: Task):
        label = LABELS[task.category]
        r = requests.post(
            f"{self.url_base}/cards?key={TRELLO_KEY}&token={TRELLO_TOKEN}&idBoard={TRELLO_BOARD}",
            data={
                'name': task.title,
                'idList': TRELLO_LIST_GENERIC,
                'idBoard': TRELLO_BOARD,
                'idLabels': [label, ],
            },
        )
        return r.status_code


    def get_random_member(self):
        r = requests.get(
            f"{self.url_base}/boards/{TRELLO_BOARD}/memberships?key={TRELLO_KEY}&token={TRELLO_TOKEN}"
        )
        members = r.json()
        member = random.choice(members)
        return member["idMember"]



trello_service = TrelloService()




