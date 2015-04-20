import scrabble

# Make a list of the highest scoring word that starts with each letter.

# This is a bit more advanced, but you already know how to do every
# single piece of this.

# This only returns 1 word with the given score.

expensive_word = {}
expensive_word_score = {}

for word in scrabble.wordlist:
    first_letter = word[0]
    if first_letter not in expensive_word:
        expensive_word[first_letter] = ''
        expensive_word_score[first_letter] = 0

    score = 0
    for char in word:
        score = score + scrabble.scores[char]

    if expensive_word_score[first_letter] < score:
        expensive_word[first_letter] = word
        expensive_word_score[first_letter] = score

for key in expensive_word:
    print(key + ": " + expensive_word[key] + ", " + str(expensive_word_score[key]))
