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


    