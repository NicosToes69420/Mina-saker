from pathlib import Path

def file_menu():
    while True:
        try:
            choice = int(input("Enter a choice: \n 1:Hume \n 2:annat "))

            match choice:
                case 1:
                    txt_path = Path(
                        "/home/nicolai/PycharmProjects/Mina-saker-Localtree/Books/Dialogues concerning second religion.txt")
                    return txt_path
                case 2:
                    txt_path = Path("/home/nicolai/PycharmProjects/Mina-saker-Localtree/Books/David_hume_complete_works.txt")
                    return txt_path
                case _:
                    print("Please enter a number")


        except ValueError:
            print("Please enter a number")


def paragraph(txt_path):
    count = 0
    paragraph = {"paragraph": {} }
    with txt_path.open("r", encoding="utf-8") as file:

        for line in file:

            if line == "\n":
                count += 1

    print(count)

