import pickle


class _FileMetaData:
    def __init__(self, count, file_name):
        self.count = count
        self.file_name = file_name

    def __str__(self):
        return f"Line count: {self.count}; File name: {self.file_name}"


def create_file(file_name):
    count_txt = 0
    with open(f"{file_name}.txt", 'w') as f:
        user_input = input("Введите строку ")
        while user_input != 'quit':
            user_input = input("Введите строку ")
            f.write(f'{user_input}\n')
            count_txt += 1

    with open('metadata.pkl', 'wb') as f:
        pickle.dump(_FileMetaData(count_txt, file_name), f)

    with open(f"{file_name}.txt", 'r') as f:
        print(f'file: {f.read()}')

    with open('metadata.pkl', 'rb') as f:
        print(f'metadata: {pickle.load(f)}')
