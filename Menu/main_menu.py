
from Statistics import *
from text_selection import file_menu


#print(f"{line} \n {Text[0]:^20}\n{line}\n {Text[1]:^10}\n {Text[2]:^20} \n {Text[3]:^10} \n {Text[4]:^20} "
#      f"\n {Text[5]:^10} \n {Text[6]:^10} \n {Text[7]:^5} \n {line}" )
def main_menu_print(file):

    Text = ["TEXT ANALYSER", "1. Load text file", "2. Display basic statistics", "3. Word frequency analysis",
            "4. Sentence analysis"
        , "5. Character analysis", "6. Export results", "7. Exit"]
    line = "=" * 20
    if file == False:
        print(f"{line} \n {Text[0]:^20}\n{line} ")

    else:
        print(f"{line} \n {Text[0]:^20}\n{line} \n You've selected {file}")

    for item in Text[1:]:
        print(f"{item:^5}")



def wait_to_return():
    g = input("press enter to return to main menu")



def load_text_file():
    txt_path = False
    while True:
        try:
            main_menu_print(txt_path)
            user = int(input("choose something bro"))
            match user:
                case 1:
                    txt_path = file_menu()

                case 2:
                    try:
                        print(statistics_run(txt_path))
                        wait_to_return()
                    except:
                        print("Välj en text fil först")


        except ValueError:
            print("Please enter a number")
load_text_file()