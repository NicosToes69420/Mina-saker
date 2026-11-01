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
    sorted_items = sorted(counter.items(), #items() = key,value i en tuple #index[1] = value, inedex[0] hade varit key
                          key=lambda item: item[1], #lamba betyder att funktionen tar en annonym variabel.
                          reverse=True)[:10]

    for word, rank in sorted_items:
        top_10_words[word] = rank

    return top_10_words

def longest_and_shortest(counter):
    longest = max(counter.keys(), key = len)
    shortest = min(counter.keys(), key = len)
    return len(longest), len(shortest)

#skriver ut vilka ord som förekommer endast en gång
def word_once(counter):
    once_words = dict()
    for ordet, antal  in counter.items():
        if antal == 1: #count är varje keys value
            once_words[ordet] = antal
    return once_words



#print( longest_and_shortest(word_counter(file_menu())) )
def word_length_distribution(counter):
    length_counter = dict()
    for ordet, antal in counter.items():
        length = len(ordet)
        length_counter[length] = length_counter.get(length, 0) + antal
    return length_counter
#print(word_length_distribution(word_counter(file_menu())))

def ui_word(txt_path):
    top10 = top_10_words(word_counter(txt_path))
    long, short = longest_and_shortest(word_counter(txt_path))
    sum_word = sum_words(word_counter(txt_path))

    once_word = sum_words((word_once(word_counter(txt_path))))
    #average word_length

    print(f"Top 10 most common words:\n")

    for rank in range(10):
        print(f"{rank}. {list(top10.keys())[rank]} ----{list(top10.values())[rank]} Times "
              f"({round ( list(top10.values())[rank]/(sum_word - list(top10.values())[rank])* 100 , 2)  }%  )")


    print(f"Word length statistics:\n Longest Word: {long} \n Shortest Word: {short} \n Average word length: {1}"
          f"\n Words appearing only once: {once_word} ")
def run_word(txt_path):
    return ui_word(txt_path)