class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_available = True  

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Available: {self.is_available}"
    
class Library:
    def __init__(self):
        self.books = []  

    def add_book(self, title: str, author: str, is_available: bool = True):
        new_book = Book(title, author)  
        new_book.is_available = is_available 
        self.books.append(new_book) 


    def list_books(self) -> list:
        return [str(book) for book in self.books]  

    def load_books(self, file_path: str):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    title, author, is_available = line.strip().split(',') 
                    self.add_book(title, author) 
                    self.add_book(title, author, is_available == 'True')
            print(f"Books successfully loaded from {file_path}.")
        except FileNotFoundError:
            print(f"The file at {file_path} was not found.")
        except Exception as e:
            print(f"An error occurred while loading the books: {e}")

    def lend_book(self, book_title: str, student: 'Student') -> bool:
        for borrowed_book in student.borrowed_books:
            if borrowed_book.title == book_title:
                print(f"{student.name} already borrowed '{book_title}'.")
                return False

        for book in self.books:
            if book.title == book_title:
                if not book.is_available:
                    print(f"'{book_title}' is currently unavailable.")
                    return False
                book.is_available = False
                student.borrowed_books.append(book)
                print(f"{student.name} borrowed '{book_title}' from the library.")
                return True

        print(f"'{book_title}' does not exist in the library.")
        return False

    def accept_return(self, book_title: str, student: 'Student'):
        for book in student.borrowed_books:
            if book.title == book_title:
                book.is_available = True
                student.borrowed_books.remove(book)
                print(f"{student.name} returned '{book_title}' to the library.")
                return

        print(f"{student.name} has not borrowed '{book_title}'.")

    def search_books(self, query: str) -> list:
        
        query_lower = query.lower()
        matching_books = [
            str(book) for book in self.books
            if query_lower in book.title.lower() or query_lower in book.author.lower()
        ]
        return matching_books

    def save_books(self, file_path: str):
        try:
            with open(file_path, 'w') as file:
                for book in self.books:
                    
                    file.write(f"{book.title},{book.author},{book.is_available}\n")
            print(f"Books successfully saved to {file_path}.")
        except Exception as e:
            print(f"An error occurred while saving the books: {e}")

class Student:
    def __init__(self, name: str, max_borrow_limit: int = 3):
        self.name = name  
        self.borrowed_books = []  
        self.borrowed_count = 0  
        self.max_borrow_limit = max_borrow_limit  

    def borrow_book(self, book_title: str, library: Library):
        if self.borrowed_count >= self.max_borrow_limit:
            print(f"{self.name} has already reached the borrowing limit of {self.max_borrow_limit} books.")
            return

        
        for book in library.books:
            if book.title == book_title and book.is_available:
                book.is_available = False  
                self.borrowed_books.append(book)  
                self.borrowed_count += 1  
                print(f"{self.name} borrowed '{book_title}'")
                return

        print(f"Sorry, '{book_title}' is not available or does not exist in the library.")

    def return_book(self, book_title: str, library: Library):
        
        for book in self.borrowed_books:
            if book.title == book_title:
                book.is_available = True  
                self.borrowed_books.remove(book)  
                self.borrowed_count -= 1 
                print(f"{self.name} returned '{book_title}'")
                return
        print(f"{self.name} has not borrowed '{book_title}'.")


def run_library_system():
    library = Library()  
    student = Student("John Doe")  
    library.load_books("python_exercise/library_data.txt")
    
    while True:
        print("\nLibrary Menu:")
        print("1. View all books")
        print("2. Search for a book")
        print("3. Add a new book")
        print("4. Borrow a book")
        print("5. Return a book")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
          
            books = library.list_books()
            if books:
                print("\nBooks in the library:")
                for book in books:
                    print(book)
            else:
                print("No books available.")
                
        elif choice == "2":
          
            query = input("Enter title or author to search: ")
            results = library.search_books(query)
            if results:
                print("\nSearch results:")
                for result in results:
                    print(result)
            else:
                print("No books found matching your query.")
        
        elif choice == "3":
       
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            is_available = input("Is the book available? (yes/no): ").strip().lower() == "yes"
            library.add_book(title, author, is_available)
            library.save_books("python_exercise/library_data.txt")
            print(f"'{title}' by {author} has been added to the library.")
        
        elif choice == "4":
       
            book_title = input("Enter the title of the book you want to borrow: ")
            if library.lend_book(book_title, student):
                print(f"{student.name} borrowed '{book_title}'.")
            else:
                print("Could not borrow the book.")
        
        elif choice == "5":
           
            book_title = input("Enter the title of the book you want to return: ")
            library.accept_return(book_title, student)
            library.save_books("python_exercise/library_data.txt")
        
        elif choice == "6":
         
            print("Exiting the library system.")
            break
        
        else:
            print("Invalid choice, please try again.")

run_library_system()

