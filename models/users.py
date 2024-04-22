from dataclasses import dataclass
from enum import Enum

USER_ADULT_AGE = 18


class Status(Enum):
    worker = 'students'
    students = 'worker'


@dataclass
class User:
    name: str
    age: int
    status: Status
    items: list[str]

    def is_adult(self):
        return self.age >= USER_ADULT_AGE

    # def __init__(self, name, age, status, items):
    #     self.name = name
    #     self.age = int(age)
    #     self.status = status
    #     self.items = items
    #


class Worker(User):
    status = Status.worker

    def __init__(self, name, age, items):
        self.name = name
        self.age = int(age)
        self.items = items

    def do_work(self):
        pass


if __name__ == '__main__':
    # Oleg;18;worker;pen
    d = {'name': 'Oleg',
         'age': 18,
         'status': 'worker',
         'items': ['pen']}

    oleg = User(name='Oleg', age=18, status=Status.students, items=['pen'])
    oleg2 = User(name='Oleg', age=18, status=Status.students, items=['pen'])
    olga = User(name='Olga', age=16, status=Status.worker, items=['book'])

    olga.worker = Worker(name='Olga', age=16, items=['book'])

    assert oleg == oleg2

    assert oleg.age == 18
    assert olga.age == 17

    olga.age += 1

    assert olga.age == 18



