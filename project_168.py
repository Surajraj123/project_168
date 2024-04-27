class book_shelf:
    def __init__(self, name, author, price, publishing_year):
        self.book_name = name
        self.author_name = author
        self.book_price = price
        self.publishing_year = publishing_year
        
    def add_book(self):
        print("Book name:- " + self.book_name)
        print("Author's name:-  " + self.author_name)
        print("Price:- " + str(self.book_price))
        print("Publishing year:- " + str(self.publishing_year))
        print("Book Added!")
        
    def year_publishing(self):
        year_age_publish = 2024 - self.publishing_year
        print("This book is published in:- " + str(year_age_publish),"years ago")

book_name1 = book_shelf("Harry Potter and the Philoshopher stone", "J.K. Rowling", 1800, 1998)
book_name1.add_book()
book_name1.year_publishing()

book_name2 = book_shelf("The diary of the Wimpy Kid", "Jeff Kiney", 700, 2017)
book_name2.add_book()
book_name2.year_publishing()