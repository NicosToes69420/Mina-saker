from text_selection import file_menu

def unique_word(txt_path):
    counter = dict()
    unique_words = []  # counter2 håller i ord och antal
    word_analysis = { "counted_words":counter } #alla ord och hur många gånger de stöts på


    with txt_path.open("r", encoding="utf-8") as hume:  #read

        for line in hume:

            for word in line.split():
                clean_word = word.lower().strip(".,!?:;'()-") #omvalndar allting en gång istället för två

                if clean_word.isalpha(): #kollar om det stripade ordet är
                    counter[clean_word] = counter.get(clean_word, 0) + 1 #ordet och hur ofta det förekommer
                    unique_words.append(clean_word) #alla ord som finns




    word_analysis = { "unique_words": list(set(unique_words)) #alla unika ord
                      ,"counted_words":counter
                      ,"top_10_words": {} #skapar en top dictionary för senare
                      ,"once_words": {}
                      }
    return word_analysis
    #Tack geeks for geeks #d = {'watermelon': 1, 'apple': 2, 'banana': 3}        asc = k: v for k, v in sorted(d.items(), key=lambda item: item[1])} print(asc)

#def word_frequency #vill inte ha så mycket i unique words

def top_10_words(word_analysis):
    sorted_items = sorted(word_analysis["counted_words"].items(),
                          key=lambda item: item[1], #lamba betyder att funktionen tar en annonym variabel.
                          reverse=True)[:10]

    #sorted items är en lista som innehåller 10 st 2-tuplar. for loopen säger bara att n-tuple med 1-1
    #ska läggas till i wordanalysis disctionary som en dicitonar för varje key (första tuple/ordet) får
    #värdet (andra tuplen/siffran).
    for k, v in sorted_items:
        word_analysis["top_10_words"][k] = v #
        #print(k, v , sorted_items, type(sorted_items))

    return word_analysis



def word_once(word_analysis):

    for ordet, antal  in word_analysis["counted_words"].items():
        if antal == 1: #count är varje keys value

            word_analysis["once_words"][ordet] = antal
    return word_analysis

#print(f"{word_once(unique_word())} hej"  )
#for word in word_once(unique_word()):
#    print(f"{word:-^20}")

#print(word_once(unique_word(file_menu())))
#print(top_10_words(unique_word(file_menu())))