def remove(word, char):
    word = word.replace(char, '')
    return word


string_old = input("Enter a word: ")
char_to_remove = input("Enter a char: ")
new_string = remove(string_old, char_to_remove)

print("Before changing:", string_old)
print("After changing:", new_string)

