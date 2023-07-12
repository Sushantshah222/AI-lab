# def count_character(sentence: str) -> dict:
#     character_count = {}
#     for char in sentence:
#         if char in character_count:
#             character_count[char] += 1
#         else:
#             character_count[char] = 1
#     return character_count


# if __name__ == "__main__":
#     sentence = "A quick brown fox jumps over a lazy dog"
#     result = count_character(sentence)
#     print(result)




sentence = "A quick brown fox jumps over a lazy dog"


def countCharacters(sentence:str)->dict:
    aDict = dict()
    for letter in sentence:
        if letter not in aDict:
            aDict[letter] = 1
        else:
            aDict[letter] =+ 1
    return aDict

print(countCharacters(sentence))