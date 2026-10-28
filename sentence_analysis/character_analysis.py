from pathlib import Path
def tecken_reknare():
    dic = {}

    file = Path("/home/nicolai/PycharmProjects/Mina-saker-Localtree/Books/Dialogues concerning second religion.txt")


    with open(file, 'r') as f:
        for line in f:
            for tecken in line.lower():
                dic[tecken] = dic.get(tecken, 0) + 1



    return dic


def sentence_analysis():
    file = Path("/home/nicolai/PycharmProjects/Mina-saker-Localtree/Books/Dialogues concerning second religion.txt")

    alla_meningar = []
    temp_mening = ""

    with open(file, 'r', encoding='utf-8') as f:

        for line in f:

            for char in line.strip("\n"): # gillar inte \n i texten
                temp_mening += char #så att varje ord, undivker problemet med att återkalla tidigare lines och komma ihåg dess position

                if char == '.' or char == '!' or char == '?': # inte helt inklusivt
                    alla_meningar.append(temp_mening)
                    temp_mening = ""



    return alla_meningar



def all_punkt(dic):
    #numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']#
    punctuation = [".", "!", "?", ",", "'", ";"]
    #others = [' ', '\n', '&']

    punctuation_sum = 0
    for punkt in punctuation:
        if punkt in dic:

            punctuation_sum += dic[punkt]

    return punctuation_sum

def filter_chars(dic):
    nya = {}
    for key in dic.keys():
        if key.isalpha():
            nya[key] = dic.get(key)


    return nya



def output_most_common_letters():

    dic_letter = filter_chars(tecken_reknare())
    #print(dic_letter)
    print('Most common letters')

    sorted_top10 = sorted(dic_letter.items(),
                          key=lambda item: item[1], #lamba betyder att funktionen tar en annonym variabel.
                          reverse=True)[:10]




    for rad in range(10):
        print(f"{rad + 1} {str(sorted_top10[rad]).strip("()").replace(",","-")}" )


def paragraph(txt_path):# vet inte var denna borde ligga
    count = 0
    paragraph = {"paragraph": count }
    with txt_path.open("r", encoding="utf-8") as file:

        for line in file:

            if line == "\n":
                count += 1
    return paragraph
