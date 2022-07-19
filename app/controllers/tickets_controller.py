import json
from fastapi import APIRouter, Response
from starlette import status
from app.services.trello_service import trello_service
from app.models.ticket import Ticket, Bug, Issue, Task

router = APIRouter()


@router.post(
    "",
    name="create task",
    status_code=status.HTTP_201_CREATED,
)
async def create_ticket(
    ticket: Ticket,
    response: Response
):
    try:
        if ticket.type=='issue':
            issue = Issue.create_from_ticket(ticket)
            trello_service.create_issue(issue)
            return ticket
        elif ticket.type=='bug':
            bug = Bug.create_from_ticket(ticket)
            trello_service.create_bug(bug)
            return bug
        elif ticket.type=='task':
            task = Task.create_from_ticket(ticket)
            trello_service.create_task(task)
            return task
        else:
            response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
            response.body = "type is not valid"
            return ticket
    except ValueError as err:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        print(str(err))
        return str(err)


    return ticket

@router.get(
    "get_board",
    name="board",
    status_code=status.HTTP_200_OK,
)
def create():
    return trello_service.get_board()
