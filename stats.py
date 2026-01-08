def count_words(text):
    num_words = len(text.split())
    print(f"Found {num_words} total words")

def count_chars(text):
    words = text.lower()
    char_dict = {}
    for word in words:
        for letter in word:
            letter_count = char_dict.get(letter, "Does not exist")
            if letter_count == "Does not exist":
                char_dict[letter] = 1
            else:
                char_dict[letter] = letter_count + 1
    
    return char_dict

def sort_on(items):
    return items["num"]

def sort_dict(dictionary):
    dict_list = []
    
    for key, value in dictionary.items():
        dict_list.append({"letter": key, "num": value})

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list




    