import re


class InvalidEmailException(Exception):
    pass


def check_email(email):
    try:
        left_part, right_part = re.split(r'@', email)
    except ValueError:
        raise InvalidEmailException('Invalid email')

    if check_left_part_email(left_part) and check_right_part_email(right_part):
        print('Valid email')
    else:
        print('Invalid email')


def check_left_part_email(left_part):
    pattern = re.compile('[\w]+')
    return pattern.match(left_part)


def check_right_part_email(right_part):
    pattern = re.compile('[\w.]+(\.(com|ru|org|net|ua))')
    return pattern.match(right_part)


def check_whole_email(email):
    pattern = re.compile('[\w]+[@]{1}[\w.]+(\.(com|ru|org|net|ua))')
    return pattern.match(email)


if __name__ == '__main__':
    inp = input("Введите email: ")
    try:
        check_email(inp)
    except InvalidEmailException as e:
        print(e)
