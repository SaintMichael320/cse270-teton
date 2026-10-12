import json
import random

pronouns = ["he", "she", "they", "I", "we"]
articles = ["a", "the"]

structures = [
    ["ART", "ADJ", "NOUN", "ADV", "VERB", "PREP", "ART", "ADJ", "NOUN"],    
    ["PRO", "ADV", "VERB", "ART", "ADJ", "NOUN", "PREP", "ART", "ADJ", "NOUN"],
    ["PRO", "ADV", "VERB", "PREP", "ART", "ADJ", "NOUN", "PREP", "ART", "ADJ", "NOUN"],
    ["PRO", "ADV", "VERB", "ART", "ADJ", "NOUN", "PREP", "ART", "ADJ", "NOUN"]
]

def get_seven_letter_word():
    result = input("Please enter a word with at least 7 letters: ")
    if len(result) < 7:
        raise ValueError
    return result.upper()

def parse_json_from_file(file_path):
    with open(file_path, 'r') as file:
        json_data = json.load(file)
        return json_data

def choose_sentence_structure():
    return random.choice(structures)

def get_pronoun():
    return random.choice(pronouns)

def get_article():
    return random.choice(articles)

def get_word(letter, speech_part):    
    return speech_part[ord(letter) - 65]

def fix_agreement(sentence):
    for index in range(len(sentence)):
        word = sentence[index]
        if word in ["he","she"]:
            sentence[index+2] = sentence[index+2] + "s"
        if word == "a":
            first_letter = sentence[index + 2][0]
            if first_letter in "aeiou":
                sentence[index] = 'an'
        if word == "the" and index == 0:            
            sentence[index + 4] = sentence[index + 4] + "s"

def build_sentence(seed_word, structure, data):
    sentence = []
    index = 0
    for part in structure:
        if part == 'ART':
            sentence.append(get_article())
        elif part == 'ADJ':
            sentence.append(get_word(seed_word[index], data["adjectives"]))
            index+=1
        elif part == 'NOUN':
            sentence.append(get_word(seed_word[index], data["nouns"]))
            index+=1
        elif part == 'VERB':
            sentence.append(get_word(seed_word[index], data["verbs"]))
            index+=1
        elif part == 'ADV':
            sentence.append(get_word(seed_word[index], data["adverbs"]))
            index+=1
        elif part == 'PREP':
            sentence.append(get_word(seed_word[index], data["prepositions"]))
            index+=1
        elif part == 'PRO':
            sentence.append(get_pronoun())
    
    fix_agreement(sentence)
    result = " ".join(sentence).capitalize()
    return result

def main():
    user_input = get_seven_letter_word()
    structure = choose_sentence_structure()
    data = parse_json_from_file("word_lists.json")
    sentence = build_sentence(user_input, structure, data)
    print(sentence)
    
if __name__ == '__main__':
    main()