import scrabble

# What is the longest word that starts with a q?

# This problem was ill-specified. What if there isn't a single longest word? What if
# there is a tie? 
# We designed this problem with that ambiguity in mind, because sometimes the thing
# we want to measure may not exist, or may not exist in the way we anticipate.

# This solution keeps EVERY word of the longest length.

longest_so_far = [] 
length_of_longest_word = 0

for word in scrabble.wordlist:

    if word[0] == 'q':
        if len(word) > length_of_longest_word:
            length_of_longest_word = len(word)
            longest_so_far = [word]
        elif len(word) == length_of_longest_word:
            longest_so_far.append(word)
            #print longest_so_far  # Use this to see the progression.

print longest_so_far
