# Wordle

![Image](https://github.com/user-attachments/assets/cace0bea-213c-4b20-9394-756b7eb8e5a0)

**Wordle GUI**

## Project Summary
Wordle Clone in Python with the ability replay games and prevent repeat entries. It additionally has a keyboard like the New York Times Wordle to assist with guessing the word. The keyboard will color based on three colors: 

- Green:  If letter is in the correct position, even if the letter is later guessed in another guess word and is in the wrong position.
- Yellow: If the letter is in the word but in the wrong position, regardless of whether a user later guesses the letter twice and one of the letters is not in the word.
- Grey: If the letter is not in the word and not previously colored as green or yellow. 

The `matplotlib` library has been used to create two visualizations. The first visualization shows the guess distribution for each attempt. For instance, across 4 games, it took the player 5 attempts to to guess the correct word. It additionally shows the following: 

- Total Games Played
- Total Games Won
- Total Games Lost
- Games Won Percentage
- Games Lost Percentage

![Image](https://github.com/user-attachments/assets/5fc520d5-acd7-4a8d-b999-e826a8818ee1)

The second visualization shows the player's most frequently guessed words:

![Image](https://github.com/user-attachments/assets/cd88a43b-e4d9-47ea-a210-9bf84940aa50)

## Project Features

This Wordle Application has some additional featuers like preventing duplicate entries. For instance, if a user types "ASSET" once, they cannot again type "ASSET". They will instead be prompted to make another guess.

![Image](https://github.com/user-attachments/assets/1853bc16-8ae1-46b2-a83e-8358f7cacee2)

### Safeguards:

Safeguards have been created to prevent the user from entering nonensical entries such as _STAWL_ or all vowels like _AEIOU_. Other safeguards are to prevent the user from accidentally wasting a guess by entering repeat words or nothing at all. Finally the last safeguard is to prevent a user from entering words greater than 5 letters which would cause the program to crash.

#### Message Safeguards
Message Safeguards are for dealing with invalid words like _STRAK_ which will prompt the following message box: 
![Image](https://github.com/user-attachments/assets/e84f7543-8d74-4e0f-b88f-8b85a716d2bb) 

It should be noted that in the image **APPLE** is a valid word, however the user on their next guess tried to enter an invalid message which prompted that warning. Afterwards the user will be prompted to make another guess.

Likewise, another similar message box will appear if the user enters words less than 5 letters.

#### No Message Safeguards

These safeguards are also intended to prevent invalid entries, however they'll simply prompt the user to enter another guess instead of displaying a message box. The following scenarios will result in another prompt box: 

- entries that have numbers or special symbols like `12`, `#$`, `1W!@`
- previously guessed words (i.e trying to guess "ASSET" twice)
- words greater than 5 letters which is dealt with by exception handling.



## File Explanations
