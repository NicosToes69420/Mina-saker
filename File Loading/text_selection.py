from pathlib import Path

def file_menu():
    while True:
        try:
            choice = int(input("Enter a choice: \n 1:Hume \n 2: Hume Complete works \n 3. Kallokain \n 4. Return"))

            match choice:
                case 1:
                    txt_path = Path(
                        "/home/nicolai/PycharmProjects/Mina-saker-Localtree/Books/Dialogues concerning second religion.txt")
                    return txt_path
                case 2:
                    txt_path = Path("/home/nicolai/PycharmProjects/Mina-saker-Localtree/Books/David_hume_complete_works.txt")
                    return txt_path
                case 3:
                    txt_path = Path("/home/nicolai/PycharmProjects/Mina-saker-Localtree/Books/Kallokain.txt")
                    return txt_path
                case 4:
                    return False
                case _:
                    print("Please enter a number")


        except ValueError:
            print("Please enter a number")





