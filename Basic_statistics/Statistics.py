from pathlib import Path
def statistics_count():
    txt_path = Path("/home/nicolai/PycharmProjects/Mina-saker-Localtree/Books/Dialogues concerning second religion.txt")  #filepath =txt
    text_stats = { "total_words": 0,
                   "total_lines": 0,
                   "total_char_no_space": 0,
                   "total_char_space": 0 }

    with txt_path.open("r", encoding="utf-8") as hume:  #read

        for line in hume:
            text_stats["total_lines"] += 1

            text_stats["total_char_space"] += len(line)

            words = line.split()
            text_stats["total_words"] += len(words)

            for word in words:
                text_stats["total_char_no_space"] += len(word)


    return text_stats



def statistics_average(text_stats): #tar statistcsen och gör en average

    # Average = sum all value // number of values

    text_stats["average_words/line"] = text_stats["total_words"] / text_stats["total_lines"]
    text_stats["average_chars/words"] = text_stats["total_char_no_space"] / text_stats["total_words"]

    average_word = text_stats["total_words"] / text_stats["total_lines"]

    #return_message = f" the average word per line is: { round( text_stats["average_word"], 2):-^5}, and the average character per word is: {round( text_stats["average_line"], 2):-^5}"

    return text_stats


