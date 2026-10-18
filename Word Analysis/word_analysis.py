from text_selection import file_menu


def unique_word(txt_path):

    counter = dict() #counter håller i ord och antal
    unique_words = []


    with txt_path.open("r", encoding="utf-8") as hume:  #read

        for line in hume:

            for word in line.split():
                clean_word = word.lower().strip(".,!?:;'()-") #omvalndar allting en gång istället för två

                if clean_word.isalpha(): #kollar om det stripade ordet är
                    counter[clean_word] = counter.get(clean_word, 0) + 1
                    unique_words.append(clean_word)




    word_analysis = { "unique_words": list(set(unique_words)) , #alla unika ord
                      "counted_words":counter #alla ord och hur många gånger de stöts på
                      ,"top_10_words": {} #skapar en top dictionary för senare
                      }

    #Tack geeks for geeks #d = {'watermelon': 1, 'apple': 2, 'banana': 3}        asc = k: v for k, v in sorted(d.items(), key=lambda item: item[1])} print(asc)

    sorted_items = sorted(word_analysis["counted_words"].items(),
                          key=lambda item: item[1], #lamba betyder att funktionen tar en annonym variabel.
                          reverse=True)[:10]


    for k, v in sorted_items:
        word_analysis["top_10_words"][k] = v


    return word_analysis



def word_once(word_analysis):
    once_words = dict()
    for ordet, antal  in word_analysis["counted_words"].items():
        if antal == 1: #count är varje keys value
            once_words[ordet] = antal

    return once_words

#print(f"{word_once(unique_word())} hej"  )
#for word in word_once(unique_word()):
#    print(f"{word:-^20}")
print(word_once(unique_word(file_menu())))
