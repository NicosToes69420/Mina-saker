
from string import punctuation

from text_selection import file_menu


def sentence_analysis(file):  # Tar in filen som den ska analysera

    alla_meningar = []
    temp_mening = ""

    with open(file, 'r', encoding='utf-8') as f:

        for line in f:

            for char in line.strip("\n"):  # gillar inte \n i texten
                temp_mening += char  # så att varje ord, undivker problemet med att återkalla tidigare lines och komma ihåg dess position

                if char == '.' or char == '!' or char == '?':  # inte helt inklusivt
                    alla_meningar.append(temp_mening)
                    temp_mening = ""

    return alla_meningar


def words_in_sentence(lst):  # skickar till average_words_per_sentence() och dick_of_sente_to_len() och longest_and_shortest_sentence() #input från sentence_analysis()
    words_per_sentence = []

    for sentence in lst:
        words_per_sentence.append(len(sentence.split()))

    return words_per_sentence #ickesorterad #lista

def average_words_per_sentence(lst):  # Input från words_in_sentence() #tar frånb sentence analysis

    all_words = 0
    average_sentence = 0
    words_per_sentence = []

    for sentence in lst:
        words_per_sentence.append(len(sentence.split()))
        #print(sentence.split())
    for i in words_per_sentence:
        all_words += i
    #print(all_words, words_per_sentence)
    average_sentence = round(all_words / len(lst), 2)

    return average_sentence
#average_words_per_sentence(sentence_analysis(file_menu()))



def print_total_sentences(lst):  # Input lista med alla sentences
    print(f'Total sentences: {len(lst)}')



def dic_of_sentence_to_len(lst_words, lst_len):  # skickas till print_longest_sentence_text() #input från sentence_analysis() #input från words_in_sentence()

    dic_with_len_as_key = dict()

    for i in range(0, len(lst_len)):
        dic_with_len_as_key[lst_len[i]] = lst_words[i]

    return dic_with_len_as_key #keys: längden/antal ord, values: meningen





def longest_shortest_word_sentence(words_in_sentence): #tar från
    return min(words_in_sentence), max(words_in_sentence)


def longest_shortest_sentence_text(dic): # input från dick_of_sente_to_len()
    return dic[max(dic)], dic[min(dic)]

def ui_sentence(txt_path):

    print(f'--- Sentence Analysis for "{txt_path}" ---')
    print()
    lst = sentence_analysis(txt_path)

    print_total_sentences(lst)

    avg_words = average_words_per_sentence(lst)
    print(f'Average words per sentence: {avg_words}')
    words_per_sentence = words_in_sentence(lst)

    length_and_sentence = dic_of_sentence_to_len(lst, words_per_sentence)
    shortest_len, longest_len = longest_shortest_word_sentence(words_per_sentence)
    print(f'Shortest sentence (word count): {shortest_len}')
    print(f'Longest sentence (word count): {longest_len}')
    print()
    longest_text, shortest_text = longest_shortest_sentence_text(length_and_sentence)
    print(f'Longest sentence text:\n"{longest_text.strip()}"')
    print()
    print(f'Shortest sentence text:\n"{shortest_text.strip()}"')
    print()
    print(f'Generating sentence analysis visualisation... ')
    print()


def run_sentence(txt_path):

    ui_sentence(txt_path)


""" 

dic_of_sentence_to_len(sentence_analysis(file_menu()), words_in_sentence(sentence_analysis(file_menu())) ) 
def sentence_analysis(file):
    print(f'--- Sentence Analysis for "{file}" ---')
    print()
    lst = sentence_analysis_on_file_1(file)
    print_total_sentences(lst)
    avrage_words_per_sentence(lst)
    words_per_sentence = words_in_sentence(lst)
    length_and_sentence = dic_of_sentence_to_len(lst, words_per_sentence)
    print_shortest_and_longest_sentence(length_and_sentence)
    print()
    print_longest_and_shortest_sentence_text(length_and_sentence)
    print()
    print(f'Generating sentence analysis visualisation... ')
    print()
    print('Press Enter to continue...') """