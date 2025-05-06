import json
class books():
    def __init__(self):
        self.Author=""
        self.name="Henry"
        self.title=""
        self.Books={}
        self.price=0
    def Add(self):
     self.title=input("what book would you add")
     print("You successly add", self.title)
    
     self._Name=input("enter the name of the book you would like to add:\n").upper
     self._Author=input("enter the Author of the book you have just added:\n").upper
     self._Price=float(input("Enter the listing price of the book:\n"))
     self._Book[self.title]={'Author':self._Author, 'price':self._Price}
     print(self._Book)

    def sell(self):
        self.name=input("enter the name of the book you sell")
        try:
          str(self.name)
          if self.name in self.Books:
             self.Book.pop(self.name)
             print("the remaining book are:",self.Books)
        except:
           print("enter a book title")
    def showbook(self):
        for x in self.Books:
          print(self.Books)[x]
          print(self.Books)[x]['Author']
          print(self.Books)[x]['price']
    def save_to_file(self, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.Books, f, indent=4)
            print(f"Bookstore data saved to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")
    


