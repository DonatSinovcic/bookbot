def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    character_count_dict = get_character_count(text)

    character_list = []
    for key, value in character_count_dict.items():
        if key.isalpha():
            character_list.append({"char": key, "num": value})
    character_list.sort(reverse=True, key=sort_on)

    for item in character_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def sort_on(d):
    return d["num"]

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    lowered_text = text.lower()
    character_count_dict = {}
    for letter in range(0, len(lowered_text)):
        if lowered_text[letter] in character_count_dict:
            character_count_dict[lowered_text[letter]] += 1
        else:
            character_count_dict[lowered_text[letter]] = 1
    return character_count_dict

main()
