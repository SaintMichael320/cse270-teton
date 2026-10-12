import pytest
import json
from build_sentences import (
    get_seven_letter_word,
    parse_json_from_file,
    choose_sentence_structure,
    get_pronoun,
    get_article,
    get_word,
    fix_agreement,
    build_sentence,
    pronouns,
    articles,
    structures
)

def test_get_seven_letter_word_valid(mocker):
    mock_input = mocker.patch("builtins.input", return_value="computer")
    result = get_seven_letter_word()
    assert result == "COMPUTER"
    mock_input.assert_called_once()

def test_get_seven_letter_word_invalid(mocker):
    mocker.patch("builtins.input", return_value="short")
    with pytest.raises(ValueError):
        get_seven_letter_word()

def test_parse_json_from_file_with_tmp_path(tmp_path):
    test_data = {"adjectives": ["happy"], "nouns": ["dog"]}
    file_path = tmp_path / "word_lists.json"
    file_path.write_text(json.dumps(test_data))
    
    result = parse_json_from_file(file_path)
    assert result == test_data

def test_parse_json_from_file_not_found():
    with pytest.raises(FileNotFoundError):
        parse_json_from_file("non_existent_file_12345.json")

def test_parse_json_from_file_decode_error(tmp_path):
    file_path = tmp_path / "bad_json.json"
    file_path.write_text("invalid json content")
    with pytest.raises(json.JSONDecodeError):
        parse_json_from_file(file_path)

def test_choose_sentence_structure():
    structure = choose_sentence_structure()
    assert structure in structures

def test_get_pronoun():
    p = get_pronoun()
    assert p in pronouns

def test_get_article():
    a = get_article()
    assert a in articles

def test_get_word():
    speech_part = ["apple", "banana", "cherry"]
    assert get_word('A', speech_part) == "apple"
    assert get_word('B', speech_part) == "banana"

def test_fix_agreement():
    # Test Rule 1: "he" or "she" adds 's' to verb two words ahead
    sentence1 = ["he", "quickly", "run", "in", "the", "park"]
    fix_agreement(sentence1)
    assert sentence1[2] == "runs"

    # Test Rule 2: "a" changes to "an" if word two words ahead starts with a vowel
    sentence2 = ["a", "very", "apple"]
    fix_agreement(sentence2)
    assert sentence2[0] == "an"

    # Test Rule 3: "the" at index 0 adds 's' to verb 4 words later
    sentence3 = ["the", "quick", "brown", "fox", "jump"]
    fix_agreement(sentence3)
    assert sentence3[4] == "jumps"

def test_build_sentence():
    seed_word = "ABCDEFGHI"
    structure = ["PRO", "ADV", "VERB", "ART", "ADJ", "NOUN", "PREP", "ART", "ADJ", "NOUN"]
    data = {
        "adjectives": ["fast", "slow", "tall", "short", "big", "small", "loud", "quiet", "bright", "dark"],
        "nouns": ["cat", "dog", "bird", "fish", "tree", "car", "house", "book", "pen", "desk"],
        "verbs": ["run", "walk", "jump", "sleep", "eat", "drink", "read", "write", "speak", "listen"],
        "adverbs": ["quickly", "slowly", "happily", "sadly", "loudly", "quietly", "bravely", "calmly", "eagerly", "softly"],
        "prepositions": ["in", "on", "at", "by", "with", "under", "over", "through", "between", "among"]
    }
    
    sentence = build_sentence(seed_word, structure, data)
    assert isinstance(sentence, str)
    assert sentence[0].isupper()