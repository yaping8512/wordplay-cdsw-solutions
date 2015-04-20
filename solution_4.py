import scrabble

# Find words that match a**e*y.

for word in scrabble.wordlist:
    if len(word) == 6 and word[0] == 'a' and word[3] == 'e' and word[5] == 'y':
        print(word)
