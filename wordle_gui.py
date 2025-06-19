#-----------------------------------------------------------------------------------------------
# Import libraries
import random as r
import turtle
import os
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import official_wordle_function as owf # Custom function that I created in another script

# Create a few text files for storing player statistics.

# Set Folder Path, where file will be stored.
folder_path = r"C:\Users\varun\Box Sync\Programming Practice Python\Python Projects\Wordle"

# List all the files in the folder
files = os.listdir(folder_path)

if 'frequent_guesses.txt' not in files: # If the file is already created, then python will skip over this statement
    with open(os.path.join(folder_path,"frequent_guesses.txt"),"w"):
        pass # We just want to create an empty file, so pass will be put here.
if 'wordle_stats.txt' not in files:
    with open(os.path.join(folder_path,"wordle_stats.txt"),"w"):
        pass

# Read in word file which contains all the 5 letter words:
with open(r"C:\Users\varun\Box Sync\Programming Practice Python\Python Projects\Wordle\5_letter_words.txt","r") as word_file:
    words = word_file.readlines() # File handler is word_file. Read all of the file handler's content into a new variable called words.
# After the file handler is done, file will be automatically closed.

# Strip the newline character from each element in the list (with open context manager reads the contents in as a list by default)
complete_words = [] # Final list that will contain the edited version of the words. (No Whitespace and Capitalized)

for word in words:
    removed = word.rstrip() # Remove whitespace characters, \n is on the right of every word.
    capitalized = removed.upper() # Make all the letters uppercase
    complete_words.append(capitalized) # Add the new processed letter to the complete_words list.

# Words have been edited, no need to keep the original list
del words

# Convert words to a set and then convert words to tuple afterwards to prevent accidental modifcation.
# Sets also cannot be subset which is what the choice function in random does.
complete_words = tuple(set(complete_words))
#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
# Create Turtle Screen
s = turtle.getcanvas()
turtle.title("Wordle")
#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
# Create turtle clone
regular_turtle_pen = turtle.Turtle()
title_turtle_pen = regular_turtle_pen.clone() # Create separate text pen for title, so that when we reset turtle, the title does not dissapear.
#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
# Create Functions for drawing squares, grid, messages, etc.
def square(x: float,y: float,outline: str,shape_color: str = None,pen_speed: int = None):
    regular_turtle_pen.penup()
    regular_turtle_pen.goto(x,y)
    regular_turtle_pen.pendown()
    regular_turtle_pen.pen(pencolor=outline, fillcolor=shape_color,speed=pen_speed,pensize=2)
    regular_turtle_pen.begin_fill()
    for i in range(4):
        regular_turtle_pen.forward(75)
        regular_turtle_pen.right(90)
    regular_turtle_pen.end_fill()

def write_letter(x: float,y: float,letter_color: str,letter: str,letter_font: tuple, pen_type):
    if pen_type == regular_turtle_pen:
        pen_type.penup()
        pen_type.goto(x,y)
        pen_type.color(letter_color)
        pen_type.write(letter,align="center",font=letter_font)
    elif pen_type == title_turtle_pen:
        pen_type.penup()
        pen_type.goto(x,y)
        pen_type.color(letter_color)
        pen_type.write(letter,align="center",font=letter_font)

def message_box(top_left_xcoor: float,top_left_ycoor: float,bttm_right_xcoor: 
                 float,bttm_right_ycoor: float,shape_color: str,x_letter: float,y_letter: 
                 float,text_color: str, message: str,mssg_font: tuple):
        rect = s.create_rectangle(top_left_xcoor,top_left_ycoor,bttm_right_xcoor,
                                  bttm_right_ycoor,fill=shape_color)
        mssg = s.create_text(x_letter,y_letter,fill=text_color,text=message,font=mssg_font)
        # Schedule deletion after 1500 milliseconds (1.5 seconds)
        s.after(1500, lambda: (s.delete(rect), s.delete(mssg))) # time.sleep() freezes Tkinter Canvas, so use this after function which will call the function after a specified time, enables us to draw and then undo the same drawing.

def stats_tracker(file_mode: str,file_name: str,status: str = None): # Create a function consolidate the code for reading and writing to a file
    if file_mode == "a+": # use append if a file needs to be updated
        with open(os.path.join(folder_path,file_name),file_mode) as stats:
            stats.write(f'{status},')
    elif file_mode == "r": # use append if we only want to read in a file.
        with open(os.path.join(folder_path,file_name),file_mode) as stats:
            word_stats = stats.readlines()
        return word_stats
#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
# Title Block
write_letter(-20,325,"black","WORDLE PYTHON",("Arial",80,"bold"),title_turtle_pen)
#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
# Grid Code
# tl = top left, br = bottom right
tl_x_coor = -200 
tl_x_coor_og = -200 # Original Starting Position, used to reset xgrid_coor back to original x-coor. This is required, since loop goes row by row.
tl_y_coor = 200
br_x_coor = -125
br_x_coor_og = -125 # Original Starting Position, used to reset xgrid_coor back to original x-coor. This is required, since loop goes row by row.
br_y_coor = 125
xgrid_coor_increment = 80 # How much to increment each square in a row (controls spacing of square, length of square is 75, so +5 is needed for a space between the squares)
ygrid_coor_increment = 80 # Controls moving up a row to draw the next row of squares
switch = True

for i in range(11): # The square is drawn on every other i, so we need twice the i's. Range starts from zero, so double of 6 is eleven, if we count from zero.
    if switch == True:
        for sq in range(0,5): # Draws one row of 5 squares
            s.create_rectangle(tl_x_coor,tl_y_coor,br_x_coor,br_y_coor,outline="#dcdee1")
            tl_x_coor += xgrid_coor_increment 
            br_x_coor += xgrid_coor_increment
            switch = False # When Switch if false reset values before drawing the next row of squares
    elif switch == False:
        tl_x_coor = tl_x_coor_og
        br_x_coor = br_x_coor_og
        tl_y_coor -= ygrid_coor_increment # Coordinates are opposite, lower values are drawn higher in canvas, so decrease y to draw a square higher, grid starts from bottom row.
        br_y_coor -= ygrid_coor_increment # Coordinates are opposite, lower values are drawn higher in canvas, so decrease y to draw a square higher, grid starts from bottom row.
        switch = True
#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
# Keyboard
key_locations = {}
letter_locations = {}

first_row = ("Q","W","E","R","T","Y","U","I","O","P") # Make as tuples to prevent modifications, row values should be locked in.
second_row = ("A","S","D","F","G","H","J","K","L")
third_row = ("Z","X","C","V","B","N","M")

x_coor_incrementor = 50 # Length is 45 plus 5 for spacing to the next rectangle
x_letter_coor_incrementor = 50 # Each letter should be 50 pixels away from each other

r1_switch = True # Controls which keyboard row we are drawing for, r1 = row 1, etc. True means we draw, False means we don't.
r2_switch = False
r3_switch = False

while True:
    if r1_switch == True and r2_switch == False and r3_switch == False: # Row 1
        tl_x_coor = -255 # Coordinates for first rectangle/key in Row 1
        tl_y_coor = 215
        br_x_coor = -210
        br_y_coor = 275
        for i in first_row:
            key_locations[i] = (tl_x_coor,tl_y_coor,br_x_coor,br_y_coor)
            tl_x_coor += x_coor_incrementor # Length is 45 plus 5 for spacing to the next rectangle
            br_x_coor += x_coor_incrementor # Length is 45 plus 5 for spacing to the next rectangle
        x_letter_loc = -233 # Coordinates for first letter in row 1
        y_letter_loc = 244 # Coordinates for first letter
        for i in first_row:
            letter_locations[i] = (x_letter_loc,y_letter_loc)
            x_letter_loc += x_letter_coor_incrementor
        r1_switch = False # Turn off row 1, 
        r2_switch = True  # Turn on row 2
    elif r2_switch == True and r1_switch == False and r3_switch == False: # Row 2
        tl_x_coor = -230 # Coordinates for first rectangle/key in Row 2
        tl_y_coor = 280
        br_x_coor = -185
        br_y_coor = 340
        for i in second_row:
            key_locations[i] = (tl_x_coor,tl_y_coor,br_x_coor,br_y_coor)
            tl_x_coor += x_coor_incrementor 
            br_x_coor += x_coor_incrementor
        x_letter_loc = -207.5 # Coordinates for first letter in row 2
        y_letter_loc = 310
        for i in second_row:
            letter_locations[i] = (x_letter_loc,y_letter_loc)
            x_letter_loc += x_letter_coor_incrementor
        r2_switch = False
        r3_switch = True
    elif r3_switch == True and r1_switch == False and r2_switch == False: # Row 3
        tl_x_coor = -180
        tl_y_coor = 345
        br_x_coor = -135
        br_y_coor = 405
        for i in third_row:
            key_locations[i] = (tl_x_coor,tl_y_coor,br_x_coor,br_y_coor)
            tl_x_coor += x_coor_incrementor
            br_x_coor += x_coor_incrementor
        x_letter_loc = -157.5 
        y_letter_loc = 375
        for i in third_row:
            letter_locations[i] = (x_letter_loc,y_letter_loc)
            x_letter_loc += x_letter_coor_incrementor
        break

for i in key_locations: # Draw the keyboard from the two dictionaries
    loc = key_locations[i] # Retrieve the location values associated with each key.
    s.create_rectangle(*loc,outline="#DBEAFE",fill="#DBEAFE") # *loc unpacks the tuple

for i in letter_locations:
    letter_loc = letter_locations[i] # Retrieve the location values associated with each letter.
    s.create_text(*letter_loc,font=("Arial",29,"bold"),fill="black",text=i,justify="center")

# Kept here, since it's apart of the keyboard as opposed to the function section.
def keyboard_color(color,range_on = True): # Function for determining keyboard color, so that we don't have to repeat the same code
    if range_on == True: # To access list_letter and the letters specifically, we need to do slicing which requires integers, range function will be used to assist with that.
        keyboard_letter = list_letter[gu][0]
        keyboard_loc = key_locations[keyboard_letter]
        keyletter_loc = letter_locations[keyboard_letter]
        rect = s.create_rectangle(*keyboard_loc,outline="#DBEAFE",fill=color)
        text = s.create_text(*keyletter_loc,font=("Arial",29,"bold"),fill="white",text=list_letter[gu][0],justify="center")
        return rect,text # These values need to be returned, so that we can delete the colors and text in the keyboard.
    else: # This code is if the user wins
        keyboard_loc = key_locations[win] # win is the iterator used for when the user wins
        keyletter_loc = letter_locations[win]
        rect = s.create_rectangle(*keyboard_loc,outline="#DBEAFE",fill=color)
        text = s.create_text(*keyletter_loc,font=("Arial",29,"bold"),fill="white",text=win,justify="center")
        return rect,text
#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
# Main Wordle Loop
play_again = "YES"
keyboard_positions = [] # Create empy list to store the id's of the rectangle colors and text in the keyboard when playing wordle. Needed for first ieration.
while play_again == "YES" or play_again == "Y":
    xgrid_coor = -200
    ygrid_coor = 275
    xletter_coor = -162
    yletter_coor = 212
    switch = True
    tries = 1
    if keyboard_positions != []: # Needed to prevent list which has the id's to be deleted from being cleared.
        for pos in range(len(keyboard_positions)):
            shape = keyboard_positions[pos][0] # function returns tuple with shape being first element and letter being second element.
            letter = keyboard_positions[pos][1]
            s.delete(shape)
            s.delete(letter)
        keyboard_positions.clear() # Clear the list, so that we can store the new rectangle id's and text and delete them.
    correct_pos = [] # In the word, correct position
    incorrect_pos = [] # In the word, wrong position
    invalid_pos = [] # Not in the word at all
    previous_words = [] # Store word entries, so that the program can prevent repeat entries
    regular_turtle_pen.clear() # Clear all the squares and text in squares for next game
    answer = r.choice(complete_words) # Randomly select a word from this list
    g = turtle.textinput("5 Letter Word",f'guess {tries}')
    g = g.upper()
    while True:
        while (len(g) < len(answer) and (g.isalpha() == True)) or ((g.isalpha() == False)) or ((len(g) == len(answer)) and g not in complete_words) or (g in previous_words):
        # Words less than 5 letters with valid alphanumeric characters are not allowed
            if len(g) < len(answer) and (g.isalpha() == True): 
                message_box(-101,-301,94.5,-250,"black",-3,-277,"white","not enough letters",("Arial",16,"normal"))
                g = turtle.textinput("5 Letter Word",f'guess {tries}')
                g = g.upper()
    # If the user accidentally enters invalid entries sequentially, they'll be stuck in this loop until they enter a valid entry which will cause the loop to close.
            elif (g.isalpha() == False): # isalpha checks if any letters are in word. If special characters or nothing (len = 0) is there, it returns false.
                g = turtle.textinput("5 Letter Word",f'guess {tries}')
                g = g.upper()
            elif (len(g) == len(answer)) and g not in complete_words: # Basically these while loops will force a user to remain in the loop until they enter a word that does not meet the condition of the while loop. The while loops have been built this way to prevent users from entering invalid entries or trying to cheat by only entering one letter a or certain word combinations like only vowels: aeiou.
                message_box(-101,-301,94.5,-250,"black",-3,-277,"white","word not in word list",("Arial",16,"normal"))
                g = turtle.textinput("5 Letter Word",f'guess {tries}')
                g = g.upper()
            elif g in previous_words: # Prevent the user from entering repeat words
                g = turtle.textinput("5 Letter Word",f'guess {tries}')
                g = g.upper()
        
        if g != answer:
            try:
                previous_words.append(g)
                list_letter = owf.wordle(answer,g)
                stats_tracker(file_mode="a+",file_name="frequent_guesses.txt",status=g)
                for letter in list_letter:
                    if len(letter) == 1:
                        square(xgrid_coor,ygrid_coor,outline = "#dcdee1",shape_color = "#6ca965",pen_speed=10)
                        xgrid_coor += 80
                        correct_pos.append(letter)
                    elif len(letter) == 2:
                        square(xgrid_coor,ygrid_coor,outline = "#dcdee1",shape_color = "#c8b653",pen_speed=10)
                        xgrid_coor += 80
                        l = letter.strip("*")
                        incorrect_pos.append(l)
                    elif len(letter) == 3:
                        square(xgrid_coor,ygrid_coor,outline = "#dcdee1",shape_color = "#787c7f",pen_speed=10)
                        xgrid_coor += 80
                        le = letter.strip("**")
                        invalid_pos.append(le)
                for guess_letter in g:
                    gl = guess_letter
                    write_letter(xletter_coor,yletter_coor,"White",gl,letter_font=("Arial",32,"bold"),pen_type=regular_turtle_pen)
                    xletter_coor += 80
                    switch = False
                for gu in range(len(list_letter)):
                    if list_letter[gu][0] in correct_pos:
                        green = keyboard_color("#6ca965") # store as varaible so that we can add to keyboard_positions_list. (The rectangle will still be drawn on the screen due to hte s.create_rectangle method in the function.)
                        keyboard_positions.append(green) # list will store the id's so that we can delete them later, if the player choses to play a new game.
                    elif list_letter[gu][0] in incorrect_pos and (list_letter[gu][0] not in correct_pos):
                        yellow = keyboard_color("#c8b653")
                        keyboard_positions.append(yellow)
                    elif list_letter[gu][0] in invalid_pos and (list_letter[gu][0] not in correct_pos or list_letter[gu][0] not in incorrect_pos):
                        grey = keyboard_color("#787c7f")
                        keyboard_positions.append(grey)
                tries += 1
                if tries == 7: # On the 7th try break from loop, don't this for 6th try otherwise user can't enter sixth guess.
                    message_box(-50,-295,45,-265,"black",-3,-280,"white",answer,("Arial",18,"normal"))
                    stats_tracker(status ="L",file_mode="a+",file_name="wordle_stats.txt")
                    break
                if switch == False:
                    xgrid_coor = -200
                    ygrid_coor -= 80
                    xletter_coor = -162
                    yletter_coor -= 79
                    switch = True
                g = turtle.textinput("5 Letter Word",f'guess {tries}')
                g = g.upper()
            except IndexError: # Words that are longer than 5 letters in length
                while len(g) > len(answer):
                    g = turtle.textinput("5 Letter Word",f'guess {tries}')
                    g = g.upper()
        elif g == answer:
            stats_tracker(status = "W",file_mode = "a+",file_name="wordle_stats.txt")
            for sq in range(0,5): # Draws one row of 5 squares
                square(xgrid_coor,ygrid_coor,outline = "#dcdee1",shape_color = "#6ca965",pen_speed=10)
                xgrid_coor += 80
            for letter in answer:
                l = letter
                write_letter(xletter_coor,yletter_coor,"White",l,letter_font=("Arial",32,"bold"),pen_type=regular_turtle_pen)
                xletter_coor += 80
            for win in g:
                winning = keyboard_color("#6ca965",range_on=False) # range_on = False, tells Python to execute the other half of the function for when a player wins. range_on executes the first half of the function which is when a guess does not match the answer.
                keyboard_positions.append(winning)
            if tries == 1:
                message_box(-44,-295,39,-265,"black",-3,-280,"white","Genius",("Arial",18,"normal"))
                stats_tracker(status =str(tries),file_mode="a+",file_name="wordle_stats.txt")
            elif tries == 2:
                message_box(-70,-295,63,-261,"black",-4,-279,"white","Magnificent",("Arial",18,"normal"))
                stats_tracker(status =str(tries),file_mode="a+",file_name="wordle_stats.txt")
            elif tries == 3:
                message_box(-70,-295,63,-261,"black",-4,-279,"white","Impressive",("Arial",18,"normal"))
                stats_tracker(status =str(tries),file_mode="a+",file_name="wordle_stats.txt")
            elif tries == 4:
                message_box(-70,-295,63,-261,"black",-4,-279,"white","Splendid",("Arial",18,"normal"))
                stats_tracker(status =str(tries),file_mode="a+",file_name="wordle_stats.txt")
            elif tries == 5:
                message_box(-41,-295,35,-265,"black",-3,-280,"white","Great",("Arial",18,"normal"))
                stats_tracker(status =str(tries),file_mode="a+",file_name="wordle_stats.txt")
            elif tries == 6:
                message_box(-41,-295,35,-265,"black",-3,-280,"white","Phew",("Arial",18,"normal"))
                stats_tracker(status =str(tries),file_mode="a+",file_name="wordle_stats.txt")
            break
    
    # Create Graph and Aggregate Player Stats per Game
    agg_stats = stats_tracker(file_mode="r",file_name="wordle_stats.txt") # create variable to store info from wordle_stats.txt
    agg_stats = agg_stats[0] # Variable is a list, so slice into first spot to get all the information
    agg_stats = agg_stats.split(",") # Info however is stored as a large string, so split on commas, since all the info was written into the files with commas to separate the words.

    wins = agg_stats.count("W") # Count the number of wins and loss in the file.
    loss = agg_stats.count("L")
  
    attempt_freq = [] # Empty list to store the guess distribution for each attempt. i.e across all the games it took the player 4 tries to guess the correct word for 5 separate games.
    for i in range(1,7): # Do the distribution values in order, i.e 5 games took 1 attempt, 2 games took 3, attempts, easier to make it easy to pair with the actual attempt number.
        string_value = str(i) # Convert to string because the information in the file was read in as a string
        attempt = agg_stats.count(string_value) # Count how many games there for each attempt. i.e there are 5 separate games which took 4 tries to solve.
        num_value = int(attempt) # Finally reconvert the attempts back into an integer for plotting purposes.
        attempt_freq.append(num_value) # Add to list to store all the attempt values

    attempt_freq.reverse() # Matplot lib plots from the end of the list, so we want the list reversed with smaller numbers at the end. Ensures matplot lib graphs in ascending order.

    attempt_num = list(range(1,7)) # Just create the actual attempt_numbers, i.e it took 4 attempts to solve a game, etc. This will be the x-axis.
    attempt_num.reverse() # Reverse as well, so that the attempt numbrers match up with their respective attempt_frequencies.
    attempt_num = [str(i) for i in attempt_num] # Convert to string, otherwise matplotlib will sort these values if they are numerical.
    # Create the plot 
    plt.figure() # Create distinct figure, so that the next plot does not merge with this plot.
    bars = plt.barh(attempt_num,attempt_freq,color = "grey")
    if tries < 7: # Color the specific bar based on whatever someone got. However don't do if tries is 7 because that means the user lost the game. Also will throw an Out of Index error, w/out this statement, since the list goes up to 6, but tries is 7 if user looses.
        loc = attempt_num.index(str(tries))
        bars[loc].set_color("#619F5B")
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))  # Force integer ticks on x-axis
    plt.title(label =f'Total Games: {wins + loss}, Total Games Won: {wins}, Total Games Lost: {loss}\nWin Rate: {round((wins/(wins+loss))*100,2)}%, Loss Rate: {round((loss/(wins+loss))*100,2)}%',weight = 'bold',fontsize = 18)
    plt.suptitle("Wordle Statistics",weight = 'bold',fontsize = 30)
    plt.show(block = False) # Will block the turtle GUI from running until the graph is closed out.
    
    # Prompt the player to play again
    play_again = turtle.textinput("Play Again?","Yes or No")
    play_again = play_again.upper()

#-----------------------------------------------------------------------------------------------  

#-----------------------------------------------------------------------------------------------
# Second Visualization that is created after player selects no and is done playing their games.
# Visualizations shows the top 10 frequent guess words across all the games
freq_guesses = stats_tracker(file_mode="r",file_name="frequent_guesses.txt")

if freq_guesses != []: # if file is empty, readlines() will return an empty string
    freq_guesses = freq_guesses[0]
    freq_guesses = freq_guesses.split(",")
    freq_guesses.remove('') # Remove the empty string that is in list due to comma at end of file. Not needed for graph.
    
    freq_counts = Counter(freq_guesses).most_common(10) # Get the most common 10 words and their counts, then assign to freq_counts.
    y, x = zip(*freq_counts) # Expand freq counts out and assign to y and x. y is the guesses and x is the distribution since this is a horizontal bar graph.
    
    plt.figure()
    plt.barh(y[::-1], x[::-1])  # Reverse for matplotlib top-to-bottom 
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.suptitle("Frequently Guessed Words",weight = 'bold',fontsize = 30)
    plt.show(block = False)
else: # This will only appear if player guesses word correctly on their very first wordle game.
    message_box(-300,-301,300,-250,"black",-3,-277,"white","Frequently Guessed Words Unavailable",("Arial",16,"normal"))
#-----------------------------------------------------------------------------------------------
# Keep the screen up, prevent it from closing.
turtle.done()
#-----------------------------------------------------------------------------------------------
