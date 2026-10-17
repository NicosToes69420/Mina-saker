
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
                clean_word = word.lower().strip(".,!?:;'()-") #omvalndar allting en gång istället för två
                if clean_word.isalpha(): #kollar om det stripade ordet är
                    counter[clean_word] = counter.get(clean_word, 0) + 1
                    unique_words.append(clean_word)
                    #unique_words.append(word.lower().strip(".,!?:;'()-")) #tar bort alla tecken

            #for clean_word in line.split():
                #if unique_word.isalpha(): #tar bort alla siffror som dycker upp under "word appearing once"
                    #counter[clean_word] = counter.get(clean_word.lower(), 0) + 1 #använder counter collectionen #lägger till .lower() för att den ska behandla hej och hEj som samma


    word_analysis = { "unique_words": list(set(unique_words)) , #alla unika ord
                    "counted_words":counter #alla ord och hur många gånger de stöts på
                      ,"top_10_words": {} #skapar en top dictionary för senare
                      }

    #top_10_words =  {k: v for k, v in sorted(word_analysis["counted_words"].items(), key=lambda item: item[1],reverse = True )[:10] }  #Tack geeks for geeks #d = {'watermelon': 1, 'apple': 2, 'banana': 3}        asc = k: v for k, v in sorted(d.items(), key=lambda item: item[1])} print(asc)

    sorted_items = sorted(word_analysis["counted_words"].items(),
                          key=lambda item: item[1], #lamba betyder att funktionen tar en annonym variabel.
                          reverse=True)[:10]


    for k, v in sorted_items:
        word_analysis["top_10_words"][k] = v



    #print(f"unique_words_string { word_analysis["unique_words_string"][:10] } {top_10_words }") #lade in [:10] bara för att den ska visa tio uniqa ord
    #print(word_analysis["top_10_words"])
    #return word_analysis
    #return word_analysis
    return word_analysis

def word_once(word_analysis):
    once_words = dict()
    for word, count  in word_analysis["counted_words"].items():
        if count == 1:
            once_words[word] = count

    return once_words



print( word_once(unique_word()) )


