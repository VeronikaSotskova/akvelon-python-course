import pickle

from transactions.exception import InvalidTransactionException
from transactions.manager import TransactionManager


def write_to_file(manager, name='transactions.pkl'):
    with open(name, 'wb') as f:
        pickle.dump(manager, f)


def main():
    manager = TransactionManager()

    while True:
        user_input = input("Введите имя и стоимость транзакции: ")
        if user_input == 'quit':
            break
        try:
            manager.add_transaction(user_input)
        except InvalidTransactionException as e:
            print(e)

    write_to_file(manager)

    manager.print_transaction_types()

    manager.print_money_per_type()

    manager.print_total_money()


if __name__ == '__main__':
    main()
