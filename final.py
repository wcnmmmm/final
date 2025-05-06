import json

class books():
    def __init__(self):
        self.Books = {}
        # … 其他属性 …

    def Add(self):
        self.title = input("what book would you add: ").strip()
        print("You successfully add", self.title)

        _Name   = input("enter the name of the book you would like to add:\n").strip().upper()
        _Author = input("enter the Author of the book you have just added:\n").strip().upper()
        try:
            _Price = float(input("Enter the listing price of the book:\n"))
        except ValueError:
            print("Invalid price; please enter a number.")
            return

        self.Books[self.title] = {'Author': _Author, 'price': _Price}
        print(self.Books)

    def sell(self):
        self.name = input("enter the name of the book you sell: ").strip()
        if self.name in self.Books:
            self.Books.pop(self.name)
            print("the remaining books are:", self.Books)
        else:
            print("Book not found; please enter a valid title.")

    def showbook(self):
        if not self.Books:
            print("No books in store.")
            return
        for x in self.Books:
            print("Title:", x)
            print("  Author:", self.Books[x]['Author'])
            print("  Price: $", self.Books[x]['price'])

    def Save(self):
        filename = input("Enter filename to save inventory (e.g. books.json): ").strip()
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.Books, f, indent=4, ensure_ascii=False)
            print(f"Inventory saved successfully to '{filename}'.")
        except Exception as e:
            print("Error saving inventory:", e)


    
    


