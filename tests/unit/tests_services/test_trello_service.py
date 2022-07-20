import pytest
from app.services.trello_service import trello_service
from app.models.ticket import Issue, Bug, Task, Ticket
from app.core.config import TRELLO_LIST_TODO, TRELLO_BOARD, TRELLO_LIST_GENERIC, TRELLO_LABEL_BUG
from app.core.config import LABELS

class TestTrelloService:

    @staticmethod
    def test_get_data_issue():
        issue = Issue(title="a title",description="a description")
        data = trello_service.get_data(issue, "issue")
        assert data == {
                'name': issue.title,
                'desc': issue.description,
                'idList': TRELLO_LIST_TODO,
                'idBoard': TRELLO_BOARD
            }

    @staticmethod
    def test_get_data_bug():
        ticket = Ticket()
        ticket.description="Email notification is not working"
        bug = Bug.create_from_ticket(ticket)
        data = trello_service.get_data(bug, "bug")
        data['idMembers'] = ''
        assert data == {
                'name': bug.title,
                'desc': bug.description,
                'idList': TRELLO_LIST_GENERIC,
                'idBoard': TRELLO_BOARD,
                'idLabels': [TRELLO_LABEL_BUG,],
                'idMembers': ''
            }

    @staticmethod
    def test_get_data_task():
        ticket = Ticket()
        ticket.title = "Refactor login"
        ticket.category = "Maintenance"
        task = Task.create_from_ticket(ticket)
        label = LABELS[task.category]
        data = trello_service.get_data(task, "task")
        assert data == {
                'name': task.title,
                'idList': TRELLO_LIST_GENERIC,
                'idBoard': TRELLO_BOARD,
                'idLabels': [label, ],
            }
