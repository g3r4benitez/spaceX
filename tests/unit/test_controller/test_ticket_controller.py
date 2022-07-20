import mock

from fastapi import FastAPI

from fastapi.testclient import TestClient

from app.core.initializer import start_containers
from app.api.routes.router import api_router
from app.services.trello_service import TrelloService


class TestTicketController():

    def set_test_client(self):
        app = FastAPI()
        app.container = start_containers()
        app.include_router(api_router)
        self.test_client = TestClient(app)

    def trello_service(self):
        trello_service = mock.AsyncMock(spec=TrelloService)
        return trello_service

    def test_create_ticket_invalid_type(self) -> None:
        self.set_test_client()
        with self.test_client.app.container["service_container"].trello_service.override(self.trello_service()):
            response = self.test_client.post("tasks", json={'type': 'saraza'})
            assert response.status_code == 422

    def test_create_issue_without_description(self) -> None:
        self.set_test_client()
        with self.test_client.app.container["service_container"].trello_service.override(self.trello_service()):
            response = self.test_client.post("tasks", json={
                'type': 'issue',
                'title': 'any title',
            })
            assert response.status_code == 422

    def test_create_bug_without_description(self) -> None:
        self.set_test_client()
        with self.test_client.app.container["service_container"].trello_service.override(self.trello_service()):
            response = self.test_client.post("tasks", json={
                'type': 'bug',
            })
            assert response.status_code == 422

    def test_create_task_invalid_category(self) -> None:
        self.set_test_client()
        with self.test_client.app.container["service_container"].trello_service.override(self.trello_service()):
            response = self.test_client.post("tasks", json={
                'type': 'task',
                'title': 'any title',
                'category': 'any'
            })
            assert response.status_code == 422