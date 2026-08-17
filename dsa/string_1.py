def first_non_repeating_character(input_string: str) -> str:
    dict_of_characters = dict()
    for character in input_string:
        if character in dict_of_characters:
            dict_of_characters[character] += 1
        else:
            dict_of_characters[character] = 1
    for char in input_string:
        if dict_of_characters[char] == 1:
            return char
    return "No Unique Character in the Input String"


print (first_non_repeating_character('aabccbd'))
