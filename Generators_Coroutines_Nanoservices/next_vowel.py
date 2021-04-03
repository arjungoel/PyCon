def get_vowels(filename):
    for one_line in open(filename):
        for one_char in one_line:
            if one_char.lower() in 'aeiou':
                yield one


print(get_vowels("vowels.txt"))
