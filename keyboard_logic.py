# Keyboard Rules

# 1) If letter is already in correct position, label it as green
#   - Even if the same letter is guessed again but in wrong position, key still remains green

# 2) If letter is in incorrect position, label it as yellow
#    - Should only be done if the letter was not guessed in the correct position.
#    - Ex: 
#       - answer: abbas
#       - word: aba*c**k**
#       Second "a" in aback is also within abbas, but since first a is guessed correctly, this key should still be green, not yellow.

#      -Ex: 
#       - answer: abbas
#        - word: b*,l**,i**s**,s
#       b in bliss should be yellow, since it's in abbas but it wrong location. 


# 3) If letter is not in word, label it as grey
#    - Should only be done if letter was not guessed and letter is not in incorrect or correct positions.
#    - Ex: 
#       - answer: eerie
#       - word: b,e,r**,r*,y**, r is in the word, but there are not 2 r's so one r wil be grey in the Worlde GUI
#       - However, since r is in the word, the r key in the keyboard should be yellow, not grey.
#      - y should be grey however since it's not at all in the answer word.

# This code will first check the code logic before it's implemented in the actual wordle script.

# word = ["b","e","r**","r*","y"]
# word = ["b","e","r**","r*","y**"]
# word = ['a','b','a*','c**','k**']
word = ['b*','l**','i**','s**','s']
correct_pos = [] # In the word, correct position
incorrect_pos = [] # In the word, wrong position
invalid_pos = [] # Not in the word at all 

for i in word:
    if len(i) == 1:
        correct_pos.append(i)
    elif len(i) == 2:
        letter = i.strip("*")
        incorrect_pos.append(letter)
    elif len(i) == 3:
        letter = i.strip("**")
        invalid_pos.append(letter)

correct_pos
incorrect_pos
invalid_pos

for i in range(len(word)): # See comments above, explains this code logic.
    if word[i][0] in correct_pos:
        print("Green")
    elif word[i][0] in incorrect_pos and (word[i][0] not in correct_pos):
        print("Yellow")
    elif word[i][0] in invalid_pos and (word[i][0] not in correct_pos or word[i][0] not in incorrect_pos):
        print("Grey")

