import scrabble

# See if you can tell the difference between this solution and the working solution.

max_score = 0
max_word = ''
for word in scrabble.wordlist:
    if word[0] == 'a' and word[3] == 'e' and len(word) <= 7 and len(word) >= 4:
        score = 0
        for char in word:
            score = score + scrabble.scores[char]
        if score > max_score:
            max_word = word
            max_score = score

print max_score
print max_word
