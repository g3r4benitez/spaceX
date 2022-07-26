import os
from starlette.config import Config

ROOT_DIR = os.getcwd()
_config = Config(os.path.join(ROOT_DIR, ".env"))
APP_VERSION = "0.0.1"
APP_NAME = "spaceX"
API_PREFIX = "/api"

# Env vars
IS_DEBUG: bool = _config("IS_DEBUG", cast=bool, default=False)

# TRELLO
TRELLO_URL: str = _config("TRELLO_URL", cast=str)
TRELLO_KEY: str = _config("TRELLO_KEY", cast=str)
TRELLO_TOKEN: str = _config("TRELLO_TOKEN", cast=str)
TRELLO_BOARD: str = _config("TRELLO_BOARD", cast=str)
TRELLO_LIST_TODO: str = _config("TRELLO_LIST_TODO", cast=str)
TRELLO_LIST_GENERIC: str = _config("TRELLO_LIST_GENERIC", cast=str)
TRELLO_LABEL_BUG: str = _config("TRELLO_LABEL_BUG", cast=str)
TRELLO_LABEL_MAINTENANCE: str = _config("TRELLO_LABEL_MAINTENANCE", cast=str)
TRELLO_LABEL_RESEARCH: str = _config("TRELLO_LABEL_RESEARCH", cast=str)
TRELLO_LABEL_TEST: str = _config("TRELLO_LABEL_TEST", cast=str)

LABELS = {
    'Maintenance': TRELLO_LABEL_MAINTENANCE,
    'Research': TRELLO_LABEL_RESEARCH,
    'Test': TRELLO_LABEL_TEST
}

