# ---------------------------------------------------------
#
# Do not change this file.
# Hints are provided at the bottom of this file.
#
# ---------------------------------------------------------


from book_database import Book
turing_book = Book.search('enigma')

assert type(turing_book) is Book
assert turing_book.publisher == "Princeton University."
assert len(Book.publishers) == 14


#####

print("* All assertions passed. Nice work!")
print("* Remember to sync your code to GitHub and ensure that it's there!")
print("* Have a nice week!")




### HINTS:
### -------
### 1. Before starting to code, run this file and read the error message.
### 2. Do the Simplest Thing That Can Possibly Work™ to resolve the error.
### 3. Run the file again. Use Error-Driven Development™ until all assertions pass.





