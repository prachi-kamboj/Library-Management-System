books = []

def add_book():
    print("\nAdd Book")
    title = input("Book title: ")
    author = input("Author: ")
    year = input("Year: ")
    
    books.append({
        "title": title,
        "author": author,
        "year": year,
        "status": "Available"
    })
    print("Book added successfully")

def view_books():
    if not books:
        print("\nNo books available")
        return
    
    print("\nTotal books: " + str(len(books)))
    for i in range(len(books)):
        print(str(i + 1) + ". " + books[i]['title'])
        print("   Author: " + books[i]['author'])
        print("   Year: " + books[i]['year'])
        print("   Status: " + books[i]['status'])
        print("-" * 50)

def checkout_book():
    if not books:
        print("\nNo books available")
        return
    
    view_books()
    
    choice = input("\nEnter book number to borrow: ")
    
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(books):
            if books[choice - 1]["status"] == "Available":
                books[choice - 1]["status"] = "Checked Out"
                print("Book checked out successfully")
            else:
                print("Book already checked out")
        else:
            print("Invalid book number")
    else:
        print("Please enter a valid number")

def return_book():
    if not books:
        print("\nNo books available")
        return
    
    checked_out_books = []
    for book in books:
        if book["status"] == "Checked Out":
            checked_out_books.append(book)
    
    if not checked_out_books:
        print("\nNo books checked out")
        return
    
    print("\nChecked out books:")
    for i in range(len(books)):
        if books[i]["status"] == "Checked Out":
            print(str(i + 1) + ". " + books[i]['title'])
    
    choice = input("\nEnter book number to return: ")
    
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(books):
            if books[choice - 1]["status"] == "Checked Out":
                books[choice - 1]["status"] = "Available"
                print("Book returned successfully")
            else:
                print("Book not checked out")
        else:
            print("Invalid book number")
    else:
        print("Please enter a valid number")

def main():
    print("=" * 50)
    print("LIBRARY MANAGEMENT SYSTEM")
    print("=" * 50)
    
    while True:
        print("\n" + "=" * 50)
        print("Menu:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Checkout Book")
        print("4. Return Book")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            checkout_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("\nThank you!")
            break
        else:
            print("\nInvalid choice")

if _name_ == "_main_":
    main()
