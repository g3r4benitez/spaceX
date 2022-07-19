import random

import requests
from app.core.config import TRELLO_KEY, TRELLO_TOKEN, TRELLO_BOARD, TRELLO_URL, TRELLO_LIST_TODO, TRELLO_LABEL_BUG
from app.models.ticket import Bug


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
        print(r.status_code)
        print(r.text)
        return r.status_code

    def create_issue(self, name: str, desc: str):
        r = requests.post(
            f"{self.url_base}/cards?key={TRELLO_KEY}&token={TRELLO_TOKEN}&idBoard={TRELLO_BOARD}",
            data={
                'name': name,
                'desc': desc,
                'idList': TRELLO_LIST_TODO,
                'idBoard': TRELLO_BOARD
            },

        )
        print(r.status_code)
        print(r.text)
        return r.status_code

    def create_bug(self, bug: Bug):

        # get random member

        r = requests.post(
            f"{self.url_base}/cards?key={TRELLO_KEY}&token={TRELLO_TOKEN}&idBoard={TRELLO_BOARD}",
            data={
                'name': bug.title,
                'desc': bug.description,
                'idList': TRELLO_LIST_TODO,
                'idBoard': TRELLO_BOARD,
                'idLabels': [TRELLO_LABEL_BUG,],
                'idMembers': [self.get_random_member(),]
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




