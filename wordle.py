# OFFICIAL WORLDE LOGIC SCRIPT
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
word = "abbas"
guess = "bliss"
guess_list = []

# * = letter is in word but wrong place
# ** = letter is not in word 
# no asterisk = letter is in correct position

# Initially label each letter in guess with an asterisk or no asterisk.
for i in range(0,len(guess)):
    if guess[i] == word[i]:
        guess_list.append(guess[i])
    elif guess[i] in word and (guess[i] != word[i]):
        guess_list.append(guess[i] + "*")
    elif guess[i] not in word:
        guess_list.append(guess[i] + "**")


processed_words = [] # Store any words that have been processed, so we don't process them again. Mainly intended for words with duplicate letters.
for i in range(len(guess_list)):
    # Basically only address letters with single asterisk, letter count in the guess must be greater than letter count in the actual word and the letter should not be in processed words. If it's in processed words, it has already been dealt with.
    if len(guess_list[i]) == 2 and (guess.count(guess_list[i][0]) > word.count(guess_list[i][0])) and (guess_list[i] not in processed_words):  
        wrong_pos = guess_list.count(guess_list[i]) # Get ALL the wrong positions for the letter. This is why processed list exists, since the below code will address the issue of incorrect locations for all of the same letters in the guess word.
        correct_pos = guess_list.count(guess_list[i][0])
        total_word_cnt = word.count(guess_list[i][0])
        processed_words.append(guess_list[i])
        difference = total_word_cnt - (correct_pos + wrong_pos)
        a = guess_list[i]
        if difference != 0: # If difference equals zero, this means that letter's have been labelled correctly.
            index_position = []
            abs_diff = abs(difference) # Difference will be negative, so use absolute value to make it positive.
            print("statement passed difference != 0") # Check that code worked
            for j in range(0,len(guess_list)):
                if a == guess_list[j]:
                    index_position.append(j) # Grab all the locations for a letter
                    print("Appending Letter") # Check that code worked
            for k in range(0,abs_diff): # Use difference to control how many letters are changed to single asterisk. diff determines the amount of letters to be changed to single asterisk.
                m = index_position[k]
                guess_list[m] = guess_list[m][0] + "**"

print(guess_list)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# TESTING CODE
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Wordle Function
# Exact same as Official Wordle Logic, but it has been converted to a function.
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
def wordle(word,guess):
    guess_list = []

    for i in range(0,len(guess)):
        if guess[i] == word[i]:
            guess_list.append(guess[i])
        elif guess[i] in word and (guess[i] != word[i]):
            guess_list.append(guess[i] + "*")
        elif guess[i] not in word:
            guess_list.append(guess[i] + "**")

    processed_words = []
    for i in range(len(guess_list)):
        if len(guess_list[i]) == 2 and (guess.count(guess_list[i][0]) > word.count(guess_list[i][0])) and (guess_list[i] not in processed_words):
            wrong_pos = guess_list.count(guess_list[i])
            correct_pos = guess_list.count(guess_list[i][0])
            total_word_cnt = word.count(guess_list[i][0])
            processed_words.append(guess_list[i])
            difference = total_word_cnt - (correct_pos + wrong_pos)
            a = guess_list[i]
            if difference != 0:
                index_position = []
                abs_diff = abs(difference)
                # print("statement passed difference != 0")
                for j in range(0,len(guess_list)):
                    if a == guess_list[j]:
                        index_position.append(j)
                        # print("Appending Letter")
                for k in range(0,abs_diff):
                    m = index_position[k]
                    guess_list[m] = guess_list[m][0] + "**"

    return(guess_list,"word:",word,"guess:",guess)
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

# How to Call Function
wordle("burry","blurb")

test_words = [["bliss","abbas"],["abbas","bliss"], ["eerie","every"],["every","eerie"],["berry","eerie"],["eerie","berry"],["berry","every"],
              ["every","berry"],["cedar","crepe"],["crepe","cedar"],["aback","clamp"],["clamp","aback"],["stamp","aback"],["aback","stamp"],
              ["abbas","aback"],["aback","abbas"],["aware","aback"],["aback","aware"],["asset","sassy"],["sassy","asset"],
              ["sassy","gassy"],["gassy","sassy"], ["fudgy","fussy"],["fussy","fudgy"],["furry","fudgy"],["fudgy","furry"],
              ["river","furry"],["furry","river"],["asset","aback"],["aback","asset"],["cedar","aback"],["aback","cedar"],
              ["crepe","three"],["three","crepe"],["apple","papal"],["papal","apple"],["clamp","papal"],["papal","clamp"],["seven","eerie"],
              ["eerie","seven"],["asset","washa"],["peeoy","eerie"],["peeoy","every"],["every","peeoy"],["jello","lolly"],["lolly","jello"],
              ["speed","erase"],["speed","steal"],["speed","abide"],["erase","speed"],["steal","speed"],["abide","speed"],["speed","eerie"],
              ["eerie","speed"],["burry","blurb"],["blurb","burry"]]

# Empty list to store all the outputs from the wordle function.
guess_list = []

# Use a for loop to feed all the words in test_words to wordle and then append the output to the guess list.
for i in range(0,len(test_words)):
    words = test_words[i][0]
    guesses = test_words[i][1]
    gl = wordle(words,guesses)
    guess_list.append(gl)
    
# Answer key to cross verify the words.
correct_words = [
['a**', 'b**', 'b*', 'a**', 's'],
['b*', 'l**', 'i**', 's**', 's'],
['e', 'v**', 'e*', 'r*', 'y**'],
['e', 'e**', 'r*', 'i**', 'e*'],
['e**', 'e', 'r', 'i**', 'e**'],
['b**', 'e', 'r', 'r**', 'y**'],
['e**', 'v**', 'e*', 'r', 'y'],
['b**', 'e*', 'r**', 'r', 'y'],
['c', 'r*', 'e**', 'p**', 'e*'],
['c', 'e*', 'd**', 'a**', 'r*'],
['c*', 'l**', 'a', 'm**', 'p**'],
['a**', 'b**', 'a', 'c*', 'k**'],
['a**', 'b**', 'a', 'c**', 'k**'],
['s**', 't**', 'a', 'm**', 'p**'],
['a', 'b', 'a*', 'c**', 'k**'],
['a', 'b', 'b**', 'a*', 's**'],
['a', 'b**', 'a', 'c**', 'k**'],
['a', 'w**', 'a', 'r**', 'e**'],
['s**', 'a*', 's', 's*', 'y**'],
['a*', 's*', 's', 'e**', 't**'],
['g**', 'a', 's', 's', 'y'],
['s**', 'a', 's', 's', 'y'],
['f', 'u', 's**', 's**', 'y'],
['f', 'u', 'd**', 'g**', 'y'],
['f', 'u', 'd**', 'g**', 'y'],
['f', 'u', 'r**', 'r**', 'y'],
['f**', 'u**', 'r*', 'r*', 'y**'],
['r*', 'i**', 'v**', 'e**', 'r*'],
['a', 'b**', 'a**', 'c**', 'k**'],
['a', 's**', 's**', 'e**', 't**'],
['a**', 'b**', 'a*', 'c*', 'k**'],
['c*', 'e**', 'd**', 'a*', 'r**'],
['t**', 'h**', 'r*', 'e*', 'e'],
['c**', 'r*', 'e*', 'p**', 'e'],
['p*','a**','p','a*','l*'],
['a*','p*','p','l*','e**'],
['p**', 'a**', 'p*', 'a*', 'l*'],
['c**', 'l*', 'a*', 'm**', 'p*'],
['e**', 'e', 'r**', 'i**', 'e*'],
['s**', 'e', 'v**', 'e*', 'n**'],
['w**', 'a**', 's', 'h**', 'a*'],
['e**','e','r**','i**','e*'],
['e*','v**','e','r**','y'],
['p**', 'e*', 'e', 'o**', 'y'],
['l**','o*','l','l','y**'],
['j**','e**','l','l','o*'],
['e*', 'r**', 'a**', 's*', 'e*'],
['s', 't**', 'e', 'a**', 'l**'],
['a**', 'b**', 'i**', 'd*', 'e*'],
['s*', 'p**', 'e*', 'e*', 'd**'],
['s', 'p**', 'e', 'e**', 'd**'],
['s**', 'p**', 'e**', 'e*', 'd*'],
['e**', 'e*', 'r**', 'i**', 'e*'],
['s**', 'p**', 'e*', 'e*', 'd**'],
['b', 'l**', 'u*', 'r', 'b**'],
['b', 'u*', 'r**', 'r', 'y**'],
]


# Add Color for CORRECT AND INCORRECT

# Basic color codes
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'  # This resets the color back to default

# Let’s break down what’s happening here:
# - `\033` is the escape character
# - The number between `[` and `m` defines the color
# - We always use `RESET` after colored text to prevent color bleeding into subsequent output

# Link: https://medium.com/@ryan_forrester_/adding-color-to-python-terminal-output-a-complete-guide-147fcb1c335f

# Final Code down below will print whether a word is correct or incorrect.
wrong_words = []
for i in range(0,len(correct_words)):
    if correct_words[i] == guess_list[i][0]:
        print(f"{GREEN}CORRECT{RESET}")
        a = guess_list[i][1] + guess_list[i][2]
        b = guess_list[i][3] + guess_list[i][4]
        c = guess_list[i][0]
        print("number:",i)
        print(a)
        print(b)
        print(c)
    elif correct_words[i] != guess_list[i][0]: # Guess List is basically nested tuples w/in the guess list. i represents the ith tuple, while 0 accesses the first element within each tuple which is the word list.
        print(f"{RED}INCORRECT{RESET}")
        a = guess_list[i][1] + guess_list[i][2] # 1 is word: while 2 is the actual word.
        b = guess_list[i][3] + guess_list[i][4] # 3 is guess while 4 is the actual word. 
        c = guess_list[i][0] # 0 is the actual word list.
        print("number:",i)
        print(a)
        print(b)
        print(c)
        wrong_words.append(i)

# This code only shows incorrect words.
print(f"{RED} INCORRECT WORDS {RESET}")
for i in wrong_words:
    a = guess_list[i][1] + guess_list[i][2]
    b = guess_list[i][3] + guess_list[i][4]
    c = guess_list[i][0]
    print(f"{RED} INCORRECT {RESET}")
    print(i,"\n",a,"\n",b,"\n",c)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
