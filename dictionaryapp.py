import json
from difflib import get_close_matches

data = json.load(open("D:/Aleksa/python vezbe 2/Dictionary Application/data.json", "r"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        answer = input(f"Did you mean {get_close_matches(word, data.keys()) [0]} instead? Enter Y if yes, or N if no: ")
        answer = answer.lower()
        if answer == "y":
            return data[get_close_matches(word, data.keys()) [0]]
        elif answer == "n":
            return f"{word.capitalize()} is not in the dictionary. Exiting."
        else:
            return "We didn't understand your input. Exiting."
    else:
        return "That word does not exist, please double check it."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for i in output:
        print(f"{i}\n")
else:
    print(output)


