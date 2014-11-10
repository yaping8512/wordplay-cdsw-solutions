import scrabble


# This is a solution to 5 that reuses the code in 1. 
# Whenever we can, it's good to reuse code that we already have.
# Next Saturday, we'll talk about defining functions, which is the way programmers
# re-use code.

matching_words = []


for word in scrabble.wordlist:
    if word[0] == 'a' and len(word) >= 9:
        matching_words.append(word)


# Note that I use enumerate. You should look that up online to see what it does.
for i, word in enumerate(matching_words):
    if i % 2 == 0:
	print word
            


