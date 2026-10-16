import statistics
from pathlib import Path
#from Basic_statistics.Statistics import statistics_count

def unique_word():
    word_analysis = {"unique_words_string":"", "unique_words_int": 0 }
    unique_words = []
    txt_path = Path("/home/nicolai/PycharmProjects/Mina-saker-Localtree/Books/Dialogues concerning second religion.txt")  #filepath =txt
    with txt_path.open("r", encoding="utf-8") as hume:  #read
        for line in hume:
            for word in line.split():
                unique_words.extend(word.lower())
                unique_words = list(set(unique_words))
                word_analysis["unique_words_string"] = unique_words
    print(f"unique_words_string {word_analysis["unique_words_string"]}")
    return word_analysis

unique_word()