import Library as lib

app = lib.Library()

while(True):
    app.menu()
    operation = input("Select operation: ")

    match operation:
        case "1":
            app.books()
        case "2":
            app.add()
        case "3":
            app.remove()
        case _:
            print("Invalid input. Try again!")
            continue