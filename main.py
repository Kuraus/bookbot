def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_dict_alpha = {}
    for i in chars_dict:
        if ('a' <=  i <= 'z'):
            chars_dict_alpha[i] = chars_dict[i]
    char_list = [{'char': k, 'num': v} for k, v in chars_dict_alpha.items()]
    char_list.sort(reverse=True, key=sort_on)
    print("--- Begin report og books/frankenstein.txt ---")
    print(f"{num_words} words were found in the document")
    for i in char_list:
        print(f"The \'{i['char']}\' character was found {i['num']} times")
    print("--- End report ---")
    
    #print(chars_dict)
    #for i in chars_dict:
       # if i >= "a" and i <= "z":
        #    print(f"The \'{i}\' character was found {chars_dict[i]} times")



def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]

main()
