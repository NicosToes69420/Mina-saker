#from text_selection import file_menu
from text_selection import file_menu

#skapar unique wowrd och räknar hur ofta ord förekommer
def word_counter(txt_path):

    counter = dict() #counter håller i ord och antal

    with txt_path.open("r", encoding="utf-8") as hume:  #read

        for line in hume:

            for word in line.split():
                clean_word = word.lower().strip(".,!?:;'()-") #omvalndar allting en gång istället för två

                if clean_word.isalpha(): #kollar om det stripade ordet är
                    counter[clean_word] = counter.get(clean_word, 0) + 1


    return counter


def unique_word(counter):
    return list(counter.keys()) #alla ord, inget set behövs för att en dictionary kan inte ha duplicated keys#loveFöreläsning8


def sum_words(counter):
    return sum(counter.values()) #summan av alla values i counter


#räknar ut vilka de 10 mest vanliga orden är
def top_10_words(counter):
    top_10_words = dict()
    #geeks4 for geeks  # d = {'watermelon': 1, 'apple': 2, 'banana': 3}        asc = k: v for k, v in sorted(d.items(), key=lambda item: item[1])} print(asc)
    sorted_items = sorted(counter.items(),
                          key=lambda item: item[1], #lamba betyder att funktionen tar en annonym variabel.
                          reverse=True)[:10]

    for word, spot in sorted_items:
        top_10_words[word] = spot

    return top_10_words


#skriver ut vilka ord som förekommer endast en gång
def word_once(counter):
    once_words = dict()
    for ordet, antal  in counter.items():
        if antal == 1: #count är varje keys value
            once_words[ordet] = antal



