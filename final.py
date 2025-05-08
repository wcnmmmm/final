class books:
    def __init__(self):
        self.author = "henry"
        self.name = ""  
        self.title = ""
        self.price = 0
        self.Books = {}

    def add(self):
        self.title = input("What book would you like to add: ").strip()
        print("You have added", self.title)

        key = input("Enter the **key** name of the book (will be uppercased):\n").strip().upper()
        auth = input("Enter the author of this book:\n").strip().upper()
        try:
            pr = float(input("Enter the listing price of the book:\n"))
        except ValueError:
            print("Invalid price; please enter a number.")
            return

        self.Books[key] = {'author': auth, 'price': pr}
        print("Current Inventory:", self.Books)

    def show(self):
        if not self.Books:
            print("No books in store.")
            return
        for title, info in self.Books.items():
            print(f"Title: {title}, Author: {info['author']}, Price: ${info['price']}")

    def save_to_file(self, filename):

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("TITLE,AUTHOR,PRICE\n")
                for title, info in self.Books.items():
                    line = f"{title},{info['author']},{info['price']}\n"
                    f.write(line)
            print(f"Inventory saved successfully to '{filename}'.")
        except Exception as e:
            print("Error saving inventory:", e)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            if not lines:
                print(f"File '{filename}' is empty.")
                return
            if lines[0].strip().upper() == "TITLE,AUTHOR,PRICE":
                lines = lines[1:]
            for lineno, line in enumerate(lines, start=2):
                parts = line.strip().split(',')
                if len(parts) != 3:
                    print(f"Skipping invalid line {lineno}: {line.strip()}")
                    continue
                key, auth, price_str = parts
                key = key.strip().upper()
                auth = auth.strip().upper()
                try:
                    pr = float(price_str)
                except ValueError:
                    print(f"Invalid price on line {lineno}: {price_str}")
                    continue
                self.Books[key] = {'author': auth, 'price': pr}
            print(f"Inventory loaded from '{filename}'.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print("Error loading inventory:", e)
