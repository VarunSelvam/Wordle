# Wordle

![Image](https://github.com/user-attachments/assets/cace0bea-213c-4b20-9394-756b7eb8e5a0)

**Wordle GUI**

## Project Summary
Wordle Clone in Python with the ability to replay games and prevent duplicate entries. It additionally has a keyboard like the New York Times (NYT) Wordle to assist with guessing the word. The keyboard will be colored based on three colors: 

- Green: If letter is in the correct position, even if the letter is later guessed in another guess word and is in the wrong position.
- Yellow: If the letter is in the word but in the wrong position, regardless of whether a user later guesses the letter twice and one of the letters is not in the word.
- Grey: If the letter is not in the word and not previously colored as green or yellow. 

The `matplotlib` library has been used to create two visualizations. The first visualization shows the guess distribution for each attempt after each game. For instance, across 4 games, it took the player 5 attempts to guess the correct word. It additionally shows the following: 

- Total Games Played
- Total Games Won
- Total Games Lost
- Games Won Percentage
- Games Lost Percentage

![Image](https://github.com/user-attachments/assets/5fc520d5-acd7-4a8d-b999-e826a8818ee1)

* User has yet to win a game in 2 tries which is why there is no bar for 2 tries in this visualization.

The second visualization shows the player's most frequently guessed words after the user's session is over:

![Image](https://github.com/user-attachments/assets/cd88a43b-e4d9-47ea-a210-9bf84940aa50)

## Project Features

### Replay Feature

This application does not have a time lock which enables the user to play a new Wordle game. 

**Replay Feature Ex:**

![Image](https://github.com/user-attachments/assets/f4fb3f26-d881-43d4-81b7-b148c227f814)

### Custom Messages

Wordle Application will display custom messages depending on how many attempts it took to win the game.

**Custom Message Ex:**

![Image](https://github.com/user-attachments/assets/1ac58cf1-677f-44db-b3c2-fb1260c85027)

It took the user 4 tries to win this game which is why "Splendid" is displayed in the image.

### Safeguards:

Safeguards have been created to prevent the user from entering nonsensical entries such as _STAWL_ or all vowels like _AEIOU_. Other safeguards are to prevent the user from accidentally wasting a guess by entering repeat words or nothing at all. Finally, the last safeguard is to prevent a user from entering words greater than 5 letters which would cause the program to crash.

#### Message Safeguards
Message Safeguards will display a message and then prompt the user to guess again. These scenarios will result in a message box: 

- invalid words like _STRAK_
- words less than 5 letters

**Message Box Ex**

![Image](https://github.com/user-attachments/assets/39662f09-41ee-4f34-8e05-944a47491fa0) 

It should be noted that in the image **APPLE** is a valid word, however the user on their next guess tried to enter an invalid word which prompted that warning. Afterwards the user will be prompted to make another guess. Moreover, NYT's Wordle also displays messages for these invalid entry types.

#### No Message Safeguards

These safeguards are also intended to prevent invalid entries; however they'll simply prompt the user to enter another guess instead of displaying a message box. The following scenarios will result in another prompt box:

- Blank Entries
- Entries that have numbers or special symbols like `12`, `#$`, `1W!@`
- Words greater than 5 letters which is dealt with by exception handling
- Previously guessed words (i.e. trying to guess "ASSET" twice)

**Prompt Box Ex**

![Image](https://github.com/user-attachments/assets/1853bc16-8ae1-46b2-a83e-8358f7cacee2)

(The prompt box is just the regular prompt box for entering guesses. Furthermore, the NYT will not display any message for the first 3 scenarios. The NYT's Wordle does however allow repeat entries which this application does not allow.)

## Word Logic

The Wordle application must display the correct color for each letter: 

- Green: If in word
- Yellow: If in word but wrong position
- Grey: Not in word

There however is an issue with duplicate words like _SASSY_. For instance, if there are two words:

- **Word:** ASSET
- **Guess:** SASSY

The program must correctly label each S in SASSY with the first S as the following: 

- First S: "Yellow" since it's in ASSET but in the wrong position.
- Second S should be "Grey" since the third S in SASSY is in the correct position.
- Third S is "Green" since it is in the correct position.

Python's `in` operator can be used, however the `in` operator will not consider duplicates. Consequently, Python will incorrectly state that there are 2 "yellow" S's in the word SASSY. This issue however can be solved by utilizing the following formula which will be demonstrated for the letter S in "SASSY".

- Word: ASSET
- Guess: SASSY

Correct Position (CP): 1
Wrong Position(WP): 2
Total Letter Count (TLC) in Word (ASSET): 2
Total Yellow Labelled Letters:  (TYL)

**Ex:** TYL = TLC - (CP + WP)
             TYL = 2 - (1+2)
             TYL = -1
             |TYL| = 1
             
TYL = 1 indicates that one of the yellow labelled "S" in SASSY should be changed to Grey. Additionally, if TYL = 0, this means that Python's `in` operator has labelled the correct number of yellow letters. This formula however will not work if the letter count is greater in the word compared to the guess. For instance: 

- Word: ABBAS
- GUESS: BLISS

This code will not work for "B" in Bliss because there are two letters in ABBAS. 

- Correct Position (CP): 0
- Wrong Position(WP): 1
- Total Letter Count (TLC) in Word (ABBAS): 2
- Total Yellow Labelled Letters:  (TYL)

**Ex:** 
- TYL = TLC - (CP + WP)
- TYL = 2 - (0+1)
- TYL = 1
- |TYL| = 1

The formula states that one of the yellow labelled "B" should be changed to Grey which is erroneous. There is only one "B" in BLISS which is in the wrong location, but the formula is stating that this should be colored Grey. This would consequently imply that the Word (ABBAS) has no B when this is false. The solution however is to only use this formula when the **Total Letter Count in Guess > Total Letter Count in Word**. 

**Final Formula**: TYL = TLC - (CP + WP) **if** (TLC in Guess TLC < TLC in Word)

## File Explanations: 
- **`official_wordle_function**: Contains the official wordle function to determine whether a letter should be green, yellow or grey. The script is also the Python implementation of the formula explained in **Word Logic** along with being imported into the **wordle_gui** script.

- **`official_wordle_script`**: This script runs the actual Wordle Game.

- `5_letter_words`: Contains all the 5 letter words used to validate guesses and select a word. There are approximately 13,000 5-letter words in the English Language. This file contains **9,139 words** which is **70.30%** of all 5-letter words.

- `frequent_guesses`: Tracks all the guesses made by the player for every game. Wordle GUI Script then counts the distribution for each word to determine the top 10 most guessed words.

- `keyboard_logic`: Explains the logic for coloring the keys along

- `word list links`: Contains links to the files used to compile the 5 letter word list.

- `wordle`: Testing Code for validating that the **official wordle function.py** script is correctly labelling each letter. It also has comments to provide more context on the function.

- `wordle_stats`: Records all the information about the player's stats across games.
  - "L" = Loss
  - "W" = Win
  - 1,2,3,4,5,6 = Number of guesses for an individual game. The **wordle_gui** script will count the number of 1's in the file to determine the number of games where it took the player one guess.
