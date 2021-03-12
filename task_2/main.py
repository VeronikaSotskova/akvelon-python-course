def print_n_most_freq(n):
    def print_most_freq(func):
        def wrapper(*args, **kwargs):
            freq_dict = func(*args, **kwargs)
            print(freq_dict)
            list_dict = list(freq_dict.items())
            list_dict.sort(key=lambda i: i[1], reverse=True)
            iter = n

            if n > len(list_dict):
                iter = len(list_dict)

            for j in range(iter):
                print(f"word: {list_dict[j][0]}, freq: {list_dict[j][1]}")

        return wrapper

    return print_most_freq


@print_n_most_freq(n=3)
def frequencies_of_words(sentence: str):
    words = sentence.split(" ")
    result = {}
    punctuation = '.!,? '
    for word in words:
        word_new = word.lower().strip(punctuation)
        if word_new not in result.keys():
            result[word_new] = 1
        else:
            result[word_new] += 1

    return result


frequencies_of_words('Never gonna give you up Never gonna let you down Never gonna run around')
