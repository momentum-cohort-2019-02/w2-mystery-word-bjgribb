from mystery_word_class import set_user_mystery_word, guess_check #not needed with current setup

guessed = ['i', 'l', 'a']
mystery_word = "illicit"
test_word_list = ['dog', 'camel', 'elephant', 'cockroach']

test_easy_words = [word for word in test_word_list if len(word) >= 4 and len(word) <= 6]
test_medium_words = [word for word in test_word_list if len(word) >= 6 and len(word) <= 8]
test_hard_words = [word for word in test_word_list if len(word) >= 8]
test_display = [letter if letter in guessed else "_" for letter in mystery_word]

# def test_word_randomizer(test_word_list):
assert test_easy_words == ['camel']
assert test_medium_words == ['elephant']
assert test_hard_words == ['elephant', 'cockroach']

# def test_display_output(mystery_word, guessed):
assert test_display == ['i', 'l', 'l', 'i', '_', 'i', '_']
