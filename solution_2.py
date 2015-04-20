import scrabble

# What is the longest word that starts with a q?

# This is the most common student solution, which prints the *first* occurence of
# the longest word. See solution_2_advanced.py for more info.

longest_so_far = '' # Store the longest word we've seen up to this point.

for word in scrabble.wordlist:
    if word[0] == 'q':
        if len(word) > len(longest_so_far): # Question: What if I use >= rather than > here?
            longest_so_far = word

print(longest_so_far)



I wrote below code and got more results same long as the one resulted from above code, thought it's more complicated.

import scrabble

q_list = []
for word in scrabble.wordlist:
    if word[0] == "q":
       q_list.append(word)
       
#print(q_list)

for qword in q_list:
    longest_qword = max(q_list, key = len)
    if len(qword) == len(longest_qword):
        print(qword)
