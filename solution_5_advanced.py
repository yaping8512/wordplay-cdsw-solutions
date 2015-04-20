import scrabble


# This is a solution to 5 that reuses the code in 1.  Whenever we can,
# it's good to reuse code that we already have.  In a future session,
# we'll talk about defining functions, which is the way programmers
# re-use code.

matching_words = []

for word in scrabble.wordlist:
    if word[0] == 'a' and len(word) >= 9:
        matching_words.append(word)


# Note that I use enumerate. You can look up the enumerate function
# online to see what it does. We're also using a new operating "%"
# which is the modulo operator and which is more flexible than the
# "bool" based version we used before.

for i, word in enumerate(matching_words):
    if i % 2 == 0:
        print(word)
