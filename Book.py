class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def View(self):
        return(f"BookInformation:--Title:- {self.title} \n Author:-{self.author} \n Price:-{self.price}")




title = input("Enter the book title: ")
author = input("Enter the author full name: ")
price = float(input("Enter the book price: "))
b=Book(title, author, price)
print(f"\nView Details:-\n{b.View()}")