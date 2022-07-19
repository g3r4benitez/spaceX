from fastapi import APIRouter, Response
from starlette import status
from app.services.trello_service import trello_service
from app.models.ticket import Ticket, Bug

router = APIRouter()


@router.post(
    "",
    name="create task",
    status_code=status.HTTP_201_CREATED,
    response_model=Ticket
)
async def create_ticket(
    ticket: Ticket,
    response: Response
):
    if ticket.type=='issue':
        trello_service.create_issue(ticket.title, ticket.description)
        return ticket
    elif ticket.type=='bug':
        bug = Bug.create_from_ticket(ticket)
        trello_service.create_bug(bug)
        return ticket
    elif ticket.type=='task':
        return ticket
    else:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        response.body = "type is not valid"
        return ticket

    return ticket

@router.get(
    "get_board",
    name="board",
    status_code=status.HTTP_200_OK,
)
def create():
    return trello_service.get_board()
