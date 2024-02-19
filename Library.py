class Library:
    #Constructor and Destructor
    def __init__(self): #constructor
        file = open("books.txt", "a+", encoding="utf-8")
    def __del__(self): #destructor
        file.close()

    #Menu
    def menu(self):
        print("""
        *** MENU***
        1) List Books
        2) Add Book
        3) Remove Book
        """)
    
    #Library Operations
    def books(self):
        file_to_read = open("books.txt", encoding="utf-8") #for reading operations
        for element in file_to_read:
            print(element.split(',')[0:2])
        file_to_read.close()

    def add(self):
        title = input("Book title: ")

        try:
            #split by whitespace and check all letters in the words
            author = input("Author: ")
            for word in author.split(' '):
                for char in word:
                    if(not char.isalpha()):
                        raise Exception
        except Exception:
            print("[!] Error: Author's name cannot contain numerical values!")
            return

        try:
            release_year = int(input("Release Year: "))
        except ValueError:
            print("[!] Error: Invalid input for <release year>!")
            return

        try:
            page_count = int(input("Page Count: "))
        except ValueError:
            print("[!] Error: Invalid input for <page count>!")
            return
        

        file_to_write = open("books.txt", "a+", encoding='utf-8') #for writing operations
        book = [title, author, release_year, page_count]
        file_to_write.write("\n") #jump to next line in the file
        for property in book:
            file_to_write.write(str(property) + ',')
            if(property is book[len(book) - 1]): #if property is last element of the list it doesnt write comma after the property value
                file_to_write.write(str(property))
        file_to_write.close()

    def remove(self):
        #the remove function backs up all books to file_restore. Then it writes all the books on this backed up list to the file except the book to be deleted.
        title = input("Enter a title name of the book to remove: ")
        file_to_read = open("books.txt", encoding="utf-8") #for reading operations
        file_to_write = open("books.txt", "a+", encoding='utf-8') #for writing operations
        file_restore = file_to_read.read().splitlines() 
        file_to_write.truncate(0)
        for element in file_restore:
            if(element.split(',')[0] != title):
                    file_to_write.write(element + "\n")
        
        file_to_write.close()
        file_to_read.close()