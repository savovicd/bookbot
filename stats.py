def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    char_count = dict()
    for char in text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count

def sort_on(items):
    return items["num"]


def sort_dicts(char_dict):
    #char_dict.sort(key=sort_on)
    dict_list = []
    for char in char_dict:
        if char.isalpha():
            num = char_dict[char]
            dict_list.append({"char": char, "num":num})
            dict_list.sort(reverse=True,key=sort_on)
    return dict_list
