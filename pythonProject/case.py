name = input("what is your name?").upper()

match name:
    case "Hrry" | "Hermonie" | "Ron":
        print("harrrison")
    case "Darco":
        print("chioam")
    case _:
        print("who")