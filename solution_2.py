import scrabble


# What is the longest word that starts with a q?
# This is the most common student solution, which prints the *first* occurence of
# the longest word. See solution_2_advanced.py for more info.

longest_so_far = '' # Store the longest word we've seen up to this point.

for word in scrabble.wordlist:

    if word[0] == 'q':
	if len(word) > len(longest_so_far):  # What if I use >= rather than > here?
	    longest_so_far = word
            #print word  # Use this to see the progression.


print longest_so_far
            


