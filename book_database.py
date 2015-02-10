import csv

class Book:
    
    publishers = []

    def __init__(self, title, publisher):
        self.title = title
        self.publisher = publisher

    def search(self):
        file = open("books.csv")
        reader = csv.reader(file)

        for row in reader:
            if row[3] not in Book.publishers:
                Book.publishers.append(row[3])
            for fields in row:
                if self.lower() in fields.lower():
                    return Book(row[1], row[3])

        file.close()
