import pickle


class FileMetaData:
    def __init__(self, count, file_name):
        self.count = count
        self.file_name = file_name

    def __str__(self):
        return f"Line count: {self.count}; File name: {self.file_name}"


def write_to_file(file, text):
    file.write(f'{text}\n')


def write_metadata(metadata):
    with open('metadata.pkl', 'wb') as f:
        pickle.dump(metadata, f)


def read_file(file_name):
    with open(f"{file_name}.txt", 'r') as f:
        print(f'file: {f.read()}')


def read_metadata():
    with open('metadata.pkl', 'rb') as f:
        print(f'metadata: {pickle.load(f)}')
