from pathlib import Path


def file_menu():
    cwd = Path(__file__).resolve().parent.parent #path funktion => "__file__"
    # beetyder nuvarande filen ==> resolve() gör allting till en path. ==> parent går "tillbaka" ett /

    while True:
        try:
            choice = int(input("Enter a choice: \n 1:Hume \n 2:annat "))
            try:
                match choice:
                    case 1:
                        txt_path = cwd / "Books"/"Dialogues concerning second religion.txt"

                        return txt_path

                    case 2:
                        txt_path = cwd / "Books" / "David_hume_complete_works.txt"

                        return txt_path

                    case _:
                        print("Please enter a valid choice")
            except:
                print("Invalid choice")

        except ValueError:
            print("Please enter a number")


