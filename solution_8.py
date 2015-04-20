import scrabble

# See if you can tell the difference between this solution and the broken solution.

max_score = 0
max_word = ''
for word in scrabble.wordlist:
    if len(word) <= 7 and len(word) >= 4 and word[0] == 'a' and word[3] == 'e':
        score = 0
        for char in word:
            score = score + scrabble.scores[char]
        if score > max_score:
            max_word = word
            max_score = score

print(str(max_score) + " : " + max_word)

