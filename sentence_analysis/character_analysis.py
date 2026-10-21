from pathlib import Path
def täcken_räknare():
    dic = {}
    file = Path("/Books/Dialogues concerning second religion.txt")


    with open(file, 'r') as f:
        for line in f:
            for täcken in line.lower():
                dic[täcken] = dic.get(täcken, 0) + 1



    return dic
def all_punkt(dic):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']#
    punctuation = [".", "!", "?", ",", "'", ";"]
    others = [' ', '\n', '&']


    punctuation_sum = 0
    for punkt in punctuation:
        if punkt in dic:

            punctuation_sum += dic[punkt]

    return punctuation_sum

def filter_chars(dic):
    nya = {}
    for key in dic.keys():
        if key.isalpha() == True:
            nya[key] = dic.get(key)


    return nya



def output_most_common_letters():

    dic_letter = filter_chars(täcken_räknare())
    #print(dic_letter)
    print('Most common letters')

    sorted_top10 = sorted(dic_letter.items(),
                          key=lambda item: item[1], #lamba betyder att funktionen tar en annonym variabel.
                          reverse=True)[:10]




    for rad in range(10):
        print(f"{rad + 1} {str(sorted_top10[rad]).strip("()").replace(",","-")}" )


output_most_common_letters()