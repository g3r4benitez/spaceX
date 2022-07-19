from dependency_injector import containers, providers
from app.services.trello_service import TrelloService


class ContainerService(containers.DeclarativeContainer):
    trello_service = providers.Singleton(
        TrelloService
    )