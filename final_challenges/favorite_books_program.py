"""👾💻 Welcome to the Final Challenge: Favorite Books Program!
In this challenge, you will input your top 3 favorite books, 
and the program will display them in sorted order.

Let's get started! Follow the steps below:

1️⃣ First, you'll be asked to enter the name of your favorite books.
2️⃣ After that, we'll sort the list of books and show it to you!

Good luck and have fun! 😃"""

favorite_books = []
books_number = 1

while books_number <= 3:
    book = input(f"Enter book #{books_number}: ")
    favorite_books.append(book)
    books_number += 1

favorite_books.sort()

print("\nHere are your top 3 favorite books in sorted order:")

for i in range(len(favorite_books)):
    print(f"{i + 1} - {favorite_books[i]}")
