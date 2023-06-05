# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    pass

#Решение:

def remove_exclamation_marks(s):
    return s.replace("!", "")


s = "Hi! Hello!"
result = remove_exclamation_marks(s)
print(result)

s = ""
result = remove_exclamation_marks(s)
print(result)

s = "Oh, no!!!!"
result = remove_exclamation_marks(s)
print(result)



# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    pass

# Решение:

def remove_last_em(s):
    if s.endswith("!"):
        return s[:-1]
    else:
        return s


s = "Hi!"
result = remove_last_em(s)
print(result)

s = "Hi!!!"
result = remove_last_em(s)
print(result)

s = "!Hi"
result = remove_last_em(s)
print(result)



# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    pass

# Решение:

def remove_word_with_one_em(s):
    words = s.split()
    result = []

    for word in words:
        if word.count("!") != 1:
            result.append(word)

    return " ".join(result)


s = "Hi!"
result = remove_word_with_one_em(s)
print(result)

s = "Hi! Hi!"
result = remove_word_with_one_em(s)
print(result)

s = "Hi! Hi! Hi!"
result = remove_word_with_one_em(s)
print(result)

s = "Hi Hi! Hi!"
result = remove_word_with_one_em(s)
print(result)

s = "Hi! !Hi Hi!"
result = remove_word_with_one_em(s)
print(result)

s = "Hi! Hi!! Hi!"
result = remove_word_with_one_em(s)
print(result)

s = "Hi! !Hi! Hi!"
result = remove_word_with_one_em(s)
print(result)