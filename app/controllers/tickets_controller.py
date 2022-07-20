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
            issue.id = trello_service.create_card(issue, ticket.type)
            return issue
        elif ticket.type=='bug':
            bug = Bug.create_from_ticket(ticket)
            bug.id = trello_service.create_card(bug, ticket.type)
            return bug
        elif ticket.type=='task':
            task = Task.create_from_ticket(ticket)
            task.id = trello_service.create_card(task, ticket.type)
            return task
        else:
            response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
            return ticket
    except ValueError as err:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return str(err)


    return ticket

