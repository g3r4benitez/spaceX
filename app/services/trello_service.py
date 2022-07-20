import random

import requests
from app.core.config import (TRELLO_KEY, TRELLO_TOKEN, TRELLO_BOARD, TRELLO_URL, TRELLO_LIST_TODO, TRELLO_LABEL_BUG,
TRELLO_LIST_GENERIC, TRELLO_LABEL_MAINTENANCE, TRELLO_LABEL_RESEARCH, TRELLO_LABEL_TEST)
from app.models.ticket import BaseTask, Bug, Issue, Task

LABELS = {
    'Maintenance': TRELLO_LABEL_MAINTENANCE,
    'Research': TRELLO_LABEL_RESEARCH,
    'Test': TRELLO_LABEL_TEST
}

class TrelloService:

    def __init__(self, ):
        self.url_base = TRELLO_URL

    def create_card(self, task: BaseTask, subtype: str ):
        data = self.get_data(task, subtype)
        r = requests.post(
            f"{self.url_base}/cards?key={TRELLO_KEY}&token={TRELLO_TOKEN}&idBoard={TRELLO_BOARD}",
            data=data,
        )
        response = r.json()
        return response['id']

    def get_data(self, task: BaseTask, subtype: str):
        if subtype=='issue':
            return {
                'name': task.title,
                'desc': task.description,
                'idList': TRELLO_LIST_TODO,
                'idBoard': TRELLO_BOARD
            }
        if subtype=='bug':
            return {
                'name': task.title,
                'desc': task.description,
                'idList': TRELLO_LIST_GENERIC,
                'idBoard': TRELLO_BOARD,
                'idLabels': [TRELLO_LABEL_BUG,],
                'idMembers': [self.get_random_member(),]
            }
        if subtype=='task':
            label = LABELS[task.category]
            return {
                'name': task.title,
                'idList': TRELLO_LIST_GENERIC,
                'idBoard': TRELLO_BOARD,
                'idLabels': [label, ],
            }

    def get_random_member(self):
        r = requests.get(
            f"{self.url_base}/boards/{TRELLO_BOARD}/memberships?key={TRELLO_KEY}&token={TRELLO_TOKEN}"
        )
        members = r.json()
        member = random.choice(members)
        return member["idMember"]



trello_service = TrelloService()




