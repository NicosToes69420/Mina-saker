
from pathlib import Path
#from Basic_statistics.Statistics import statistics_count

def unique_word(word_analysis=None):
    #word_analysis = {"unique_words_string":"", "unique_words_int": 0 }

    counter = dict()
    unique_words = []
    txt_path = Path("/home/nicolai/PycharmProjects/Mina-saker-Localtree/Books/Dialogues concerning second religion.txt")  #filepath =txt


    with txt_path.open("r", encoding="utf-8") as hume:  #read

        for line in hume:

            for word in line.split():
                unique_words.append(word.lower().strip(".,!?:;'\()-")) #tar bort alla tecken

            for clean_word in line.split():
                counter[clean_word] = counter.get(clean_word, 0) + 1


    word_analysis = { "unique_words_string": list(set(unique_words)) , #alla unika ord
                   "unique_words_int": len(list(set(unique_words))), #antalet unika ord
                   "counted_words":counter} #alla ord och hur många gånger de stöts på

    top_10_words =  {k: v for k, v in sorted(word_analysis["counted_words"].items(), key=lambda item: item[1],reverse = True )[:10] } #Tack geeks for geeks #d = {'watermelon': 1, 'apple': 2, 'banana': 3}        asc = k: v for k, v in sorted(d.items(), key=lambda item: item[1])} print(asc)



    print(f"unique_words_string { word_analysis["unique_words_string"][:10] } {top_10_words }") #lade in [:10] bara för att den ska visa tio uniqa ord
    #print(counter)
    #return word_analysis

unique_word()