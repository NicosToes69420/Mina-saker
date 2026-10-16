from pathlib import Path
def statistics_count():
    txt_path = Path("/home/nicolai/PycharmProjects/Mina-saker-Localtree/Books/Dialogues concerning second religion.txt")  #filepath =txt
    total_words = 0
    total_lines = 0
    total_char_no_space = 0
    total_char_space = 0
    with txt_path.open("r", encoding="utf-8") as hume:  #read

        for line in hume:
            total_lines += 1

            for char in line:
                total_char_space += 1

            for word in line.split():
                total_words += 1

                for char in word:
                   total_char_no_space += 1 #utan space

    #print(total_words, total_lines , total_char_no_space, total_char_space)
    return total_words, total_lines, total_char_no_space, total_char_space



def statistics_average(statistics_tuple): #tar statistcsen och gör en average
    # Average = sum all value // number of values
    tuple = statistics_tuple
    average_word = tuple[0] / tuple[1]
    average_line =  tuple[2] /  tuple[0]
    return_message = f" the average word per line is: { round( average_word, 2):-^5}, and the average character per word is: {round( average_line, 2):-^5}"
    return average_word, average_line, return_message


#testar
#statistics_average1 = statistics_average(statistics_count())
#print(statistics_average1[2])