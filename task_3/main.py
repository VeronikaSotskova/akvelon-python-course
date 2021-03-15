from pickle_input import input_func
from pickle_input.input_func import FileMetaData


def main():
    file_name = input("Введите имя файла: ")
    count_ = 0

    with open(f"{file_name}.txt", 'w') as f:
        user_input = input("Введите строку ")
        while user_input != 'quit':
            input_func.write_to_file(f, user_input)
            count_ += 1
            user_input = input("Введите строку ")

    input_func.write_metadata(FileMetaData(count_, file_name))

    input_func.read_file(file_name)

    input_func.read_metadata()


if __name__ == '__main__':
    main()
