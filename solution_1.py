import scrabble

# Print every word that has 9 or more letters and starts with the letter "a"

for word in scrabble.wordlist:
    if word[0] == 'a' and len(word) >= 9:
        print(word)
