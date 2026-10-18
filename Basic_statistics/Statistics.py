from pathlib import Path
def statistics_count(txt_path):

    text_stats = { "total_words": 0, "total_lines": 0, "total_char_no_space": 0, "total_char_space": 0 } #detta borde vara list?
    with txt_path.open("r", encoding="utf-8") as hume:  #read

        for line in hume:
            text_stats["total_lines"] += 1

            for char in line: #ska uttropstecken och annat räcknas med?
                text_stats["total_char_space"] += 1

            for word in line.split(): #borde man ta bort punkt?
                text_stats["total_words"] += 1

                for char in word:
                   text_stats["total_char_no_space"] += 1 #utan space

    #print(total_words, total_lines , total_char_no_space, total_char_space)
    return text_stats



def statistics_average(text_stats): #tar statistcsen och gör en average
    # Average = sum all value // number of values
    text_stats["average_word"] = text_stats["total_words"] / text_stats["total_lines"]
    text_stats["average_line"] = text_stats["total_char_no_space"] / text_stats["total_words"]


    #return_message = f" the average word per line is: { round( text_stats["average_word"], 2):-^5}, and the average character per word is: {round( text_stats["average_line"], 2):-^5}"
    return text_stats
