
# __________________________________________________________________________________________
# CHARACTER ANALYSIS
# ____________________________________________________________________

def alla_tecken_icke_filt(file):  # Tar in text fil och ger ut en dictionary som är sorterad baserat på vilket täcken som är vanligast till ovanligast (vanligaste = första) key = hur många gånger det förekomer, value = vilken char
    dic = {}
    with file.open("r", encoding="utf-8") as f:
        for line in f:
            for täcken in line.lower():
                if täcken in dic:
                    dic[täcken] += 1
                else:
                    dic[täcken] = 1

    sorted_dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

    return sorted_dic



def most_common_letters(dic):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    punctuation = [".", "!", "?", ",", "'", ";"]
    others = [' ', '\n', '&']


    letters_and_times = {}
    letter_counted = dict()
    for keys, values in dic.items():  #keys: längden/antal ord, values: tecken


        if values not in numbers and keys not in punctuation and keys not in others:
            letter_counted[keys] = letter_counted.get(keys, 0) + values


    return letter_counted




def top10_letters(dic): #tar in alla chars
    top_10_words = dict()
    #geeks4 for geeks  # d = {'watermelon': 1, 'apple': 2, 'banana': 3}        asc = k: v for k, v in sorted(d.items(), key=lambda item: item[1])} print(asc)
    sorted_items = sorted(dic.items(), #items() = key,value i en tuple #index[1] = value, inedex[0] hade varit key
                          key=lambda item: item[1], #lamba betyder att funktionen tar en annonym variabel.
                          reverse=True)[:10]

    for word, rank in sorted_items:
        top_10_words[word] = rank

    return top_10_words





def char_type_distribution(
        dic):  # Tar en dictionary vars key är antal gånger en char förekommer och value är vilke char det är. Och get tillbaks en dictionary med vilken antalk nummer, punkter .... som value och key är vilken typ char tillhör (numbers, letters, punctuation, spaces)
    character_type_distribution_dic = {'letters': 0, 'numbers': 0, 'spaces': 0, 'punctuations': 0}
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    punctuation = [".", "!", "?", ",", "'", ";"]

    for i in dic:
        if i.isalpha():
            character_type_distribution_dic['letters'] += dic[i]
        elif i in numbers:
            character_type_distribution_dic['numbers'] += dic[i]
        elif i == ' ':
            character_type_distribution_dic['spaces'] += dic[i]
        elif i in punctuation:
            character_type_distribution_dic['punctuations'] += dic[i]

    return character_type_distribution_dic


def run_char( txt_path):  # Tar dictionary med key som character
    # type och value som antal gånger den char type förekommer och printar resultat.


    dic_all = alla_tecken_icke_filt(txt_path)

    dic = most_common_letters(dic_all)

    denominator = sum(dic_all.values())
    denominator_filt = sum(dic.values())

    letters = char_type_distribution(alla_tecken_icke_filt(txt_path))




    print(f"Character Analysis for: {txt_path}  \n Letters {letters["letters"]  } ( { round (letters["letters"] / denominator * 100, 2 )} % \n"
          f"Digits {round (letters["numbers"])} ( { round (letters["numbers"] / denominator * 100, 2 )} %)  \n"
          f"spaces {round (letters["spaces"])} ({round ( letters["spaces"] / denominator * 100, 2 )} % \n"
          f"Puncuation {round( letters["punctuations"] / denominator * 100, 2 )} % \n")

    print('Character type distribution')

    for rank in range(10):
        print(f"{rank}. {list(dic.keys())[rank]} ----{list(dic.values())[rank]} Times "
              f"({round(list(dic.values())[rank] / denominator_filt * 100, 2)}%  )")

