from dataclasses import dataclass

import pytest
from api.client import MyTargetClient


@dataclass
class Settings:
    URL: str = 'https://target.my.com/'
    LOGIN: str = 'anonym.213555@mail.ru'
    PASSWORD: str = 'Lbvfcbr1!'


@pytest.fixture(scope='session')
def config() -> Settings:
    settings = Settings()

    return settings


@pytest.fixture(scope='function')
def api_client(config) -> MyTargetClient:
    return MyTargetClient(config.URL, config.LOGIN, config.PASSWORD)

