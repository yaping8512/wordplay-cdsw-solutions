import scrabble

# Find the most valuable word in the dictionary using a double-loop.

max_score = 0
max_word = ''

for word in scrabble.wordlist:
    score = 0
    for char in word:
        score = score + scrabble.scores[char]
    if score > max_score:
        max_word = word
        max_score = score

print(str(max_score) + " : " + max_word)
