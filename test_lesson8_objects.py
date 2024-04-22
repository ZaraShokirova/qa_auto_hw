import csv

import pytest

from models.users import User, USER_ADULT_AGE, Status, Worker
from provaiders import UserProvider, CsvUserProvider


@pytest.fixture
def user_provider() -> UserProvider:
    return CsvUserProvider()


@pytest.fixture
def users(user_provider) -> list[User]:
    return user_provider.get_users()


@pytest.fixture
def workers(users) -> list[Worker]:
    workers = [Worker(name=user.name, age=user.age, items=user.items)
               for user in users if user.status == Status.worker]
    return workers


def test_workers_are_adults_v3(workers):
    for worker in workers:
        worker.do_work()
        assert worker.is_adult(), f"Worker {worker.name} младше {USER_ADULT_AGE} лет"

# def user_is_adult(user: User):
#     return user.age >= USER_ADULT_AGE
