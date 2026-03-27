class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def display(self):
        status = "Available" if self.is_available else "Not Available"
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book_id, title, author):
        self.books.append(Book(book_id, title, author))
        print("Book added successfully!")

    def add_member(self, member_id, name):
        self.members.append(Member(member_id, name))
        print("Member added successfully!")

    def lend_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and book.is_available:
                book.is_available = False
                print("Book lent successfully!")
                return
        print("Book not available!")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and not book.is_available:
                book.is_available = True
                print("Book returned successfully!")
                return
        print("Invalid book ID!")

    def display_books(self):
        print("\n--- Library Books ---")
        for book in self.books:
            book.display()


# Menu-driven interface
def main():
    library = Library()

    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book\n2. Add Member\n3. Lend Book\n4. Return Book\n5. Display Books\n6. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            library.add_book(book_id, title, author)

        elif choice == 2:
            member_id = int(input("Enter Member ID: "))
            name = input("Enter Member Name: ")
            library.add_member(member_id, name)

        elif choice == 3:
            book_id = int(input("Enter Book ID to lend: "))
            library.lend_book(book_id)

        elif choice == 4:
            book_id = int(input("Enter Book ID to return: "))
            library.return_book(book_id)

        elif choice == 5:
            library.display_books()

        elif choice == 6:
            print("Exiting Library System...")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()