import scrabble

# Print the longest word where every character is unique.
# I use a double loop in this. Note that I also re-use my "longest word" logic
# from the easy solution to (2).

# See the advanced solution for a shorter way to do this.

new_words = []
for word in scrabble.wordlist:
    local_chars = {}
    seen_before = False
    for character in word:
        # have we seen this character before?
        if character in local_chars:
            seen_before = True
            break # Exit the loop early, since we've found a collision.
        # store the character
        local_chars[character] = 1

    if not seen_before:
        new_words.append(word)

# Reuse my code for longest word
longest_so_far = ''
for word in new_words:
    if len(word) > len(longest_so_far):
        longest_so_far = word

print longest_so_far
