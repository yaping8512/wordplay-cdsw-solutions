import scrabble

# Find all the words that end in 'nge'
for word in scrabble.wordlist:
    if word[-3:] == 'nge':
        print(word)
