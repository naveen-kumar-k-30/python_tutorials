class library:
    def __init__(self, lis):
        self.all_books = lis
        self.available_book = lis[:]
        self.lend_book = {}

    def disp_all_book(self):
        for book in self.all_books:
            print(book)

    def disp_avail_book(self):
        for book in self.available_book:
            print(book)

    def lend(self, name, book):
        if book not in self.all_books:
            print("Enter a valid book name")
        if book in self.available_book:
            self.lend_book.update({book: name})
            self.available_book.remove(book)
            print("u can take Book")
        else:
            print("book was already taken by " + self.lend_book[book])

    def return_book(self, book):
        del self.lend_book[book]
        self.available_book.append(book)


if __name__ == "__main__":
    lib = library(["pablo", "excobar", "pulovo", "The Life Divine", "Da Vinci Code", "The Alchemist", "Educated", "Harry Potter"])
    print("Enter a option:")
    while True:
        print("1.Display all books")
        print("2.Display available books ")
        print("3.Borrow a book")
        print("4.Return a book")
        print("5.Quit")
        user_choice = int(input())
        if user_choice == 1:
            lib.disp_all_book()
        elif user_choice == 2:
            lib.disp_avail_book()
        elif user_choice == 3:
            name = input("Enter User Name ")
            book = input("Enter Book Name")
            lib.lend(name, book)
        elif user_choice == 4:
            book = input("Enter the name of the book")
            lib.return_book(book)
        elif user_choice == 5:
            break
        else:
            print("Invalid choice")
