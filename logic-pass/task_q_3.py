def count_of_char_in_string(sentence, to_count):
    if len(to_count) > 1:
        return "char length more than 1"
    rep = 0
    for i in range(len(sentence)):
        if sentence[i] == to_count:
            rep += 1

    return rep


string = input("String: ")
char = input("Char: ")
count = count_of_char_in_string(string, char)
print(count)

