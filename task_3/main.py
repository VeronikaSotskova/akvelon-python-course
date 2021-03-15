from pickle_input import input_func
from pickle_input.input_func import FileMetaData


def main():
    file_name = input("Введите имя файла: ")
    user_input = input("Введите строку ")
    count_ = 0
    while user_input != 'quit':
        count_ += 1
        input_func.write_to_file(file_name, user_input)

    input_func.write_metadata(FileMetaData(count_, file_name))

    input_func.read_file(file_name)

    input_func.read_metadata()


if __name__ == '__main__':
    main()
