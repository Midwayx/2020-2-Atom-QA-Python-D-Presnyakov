import pytest
import random
import string


@pytest.fixture(scope='function')
def get_randint():
    yield random.randint(-100, 100)


@pytest.fixture(scope='function')
def get_randlist():
    yield [random.randint(-100, 100) for _ in range(random.randint(5, 20))]


@pytest.fixture(scope='function')
def get_randdict():
    yield {random.randint(-100, 100): random.randint(0, 100) for _ in range(random.randint(5, 20))}


@pytest.fixture(scope='function')
def get_randset():
    yield lambda: {random.randint(-100, 100) for _ in range(random.randint(50, 200))}


@pytest.fixture(scope='function')
def get_randstring():
    yield lambda size=20: ''.join(random.choice(string.ascii_lowercase) for _ in range(size))
