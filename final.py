class books():
    def __init__(self):
        self.name="Henry"
        self.title=""
        self.books={}
        self.price=0
    def Add(self):
     self.title=input("what book would you add")
     print("You successly add", self.title)
    
     self._Name=input("enter the name of the book you would like to add:\n").upper
     self._Author=input("enter the Author of the book youhave just added:\n").upper
     self._Price=float(input("Enter the listing price of the book:\n"))
     self._Book[self.title]={'Author':self._Author, 'price':self._Price}
     print(self._Book)
        