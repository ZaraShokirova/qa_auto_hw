import csv


def test_workers_are_adults():
    """
    Тестируем, что все работники старше 18 лет
    """

    with open('resource/users.csv') as f:
        users = csv.DictReader(f, delimiter=';')
        workers = [user for user in users if user['status'] == 'worker']

    for worker in workers:
        assert int(worker['age']) >= 18, f"Worker {worker['Name']} младше 18 лет"

        # workers = []
        # for user in users:
        #     if user['status'] == 'worker':
        #         workers.append(user)
        # users = list(users)
