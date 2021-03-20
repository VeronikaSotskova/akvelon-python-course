import os.path
import pickle
from functools import reduce

from transactions.exception import InvalidTransactionException


class TransactionManager:

    def __init__(self):
        self.transactions = {}
        if os.path.isfile("transactions.pkl"):
            self.transactions = read_dict_from_file().transactions

    def __str__(self):
        result = ""
        for k in self.transactions.keys():
            result += f"{k}:{self.transactions[k]}\n"
        return result

    def _read_input(self, user_input):
        try:
            name, val = user_input.rsplit(" ", 1)
            val = int(val)
        except ValueError:
            raise InvalidTransactionException("Введите сначала название, далее стоимость.")
        return Transaction(name, val)

    def add_transaction(self, user_input):
        transaction = self._read_input(user_input)
        if transaction.name in self.transactions.keys():
            self.transactions[transaction.name].append(transaction.value)
        else:
            self.transactions[transaction.name] = [transaction.value, ]

    def print_transaction_types(self):
        print(f"Transaction types: {list(self.transactions.keys())}")

    def print_money_per_type(self):
        print(list(map(lambda x: f"{x}: {reduce(lambda a, b: a + b, self.transactions[x])}", self.transactions.keys())))

    def print_total_money(self):
        print(
            f"Total amount of spent money:"
            f" {reduce(lambda a, b: a + b, map(lambda k: sum(self.transactions[k]), self.transactions.keys()))}")


class Transaction:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name}: {self.value}"


def read_dict_from_file(name='transactions.pkl'):
    with open(name, 'rb') as f:
        return pickle.load(f)
