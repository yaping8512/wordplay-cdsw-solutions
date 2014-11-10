import scrabble


# Print every other word that starts with 'a' and ends with 9
# This is the most basic implementation: keep a boolean to track whether the word
# was printed.

should_i_print = True

for word in scrabble.wordlist:
    if word[0] == 'a' and len(word) >= 9:
        if should_i_print:
            print word
            should_i_print = False
        else:
            should_i_print = True
            
