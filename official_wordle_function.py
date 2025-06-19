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

    return guess_list
