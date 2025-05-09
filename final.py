import os

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
        print("Book added successfully.")
        print("Current Inventory:", self.Books)
    def sell(self):
        self.name = input("enter the name of the book you want to sell")
        try:
            str(self.name)
            if self.name in self.Books:
                self.Books.pop(self.name)
                print("the remaining books are:",self.Books)
        except:
            print("please enter a book title")

    def show(self):
        if not self.Books:
            print("No books in store.")
            return
        for title, info in self.Books.items():
            print(f"Title: {title}, Author: {info['author']}, Price: ${info['price']}")

    def save_to_file(self, filename):
        try:
            file_dir = os.path.dirname(os.path.abspath(filename))

            if file_dir and not os.path.exists(file_dir):
                os.makedirs(file_dir)
                print(f"Created missing directory: {file_dir}")

            if not self.Books:
                print("No books to save.")
                return

            print(f"Saving to file: {filename}")
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("TITLE,AUTHOR,PRICE\n")
                for title, info in self.Books.items():
                    line = f"{title},{info['author']},{info['price']}\n"
                    print(f"Writing line: {line.strip()}")
                    f.write(line)
            print(f"Inventory saved successfully to '{filename}'.")
        except PermissionError:
            print(f"Error: Permission denied when trying to save to '{filename}'.")
        except FileNotFoundError:
            print(f"Error: The file path '{filename}' does not exist.")
        except OSError as e:
            print(f"Error: OS error occurred: {e}")
        except Exception as e:
            print(f"Unexpected error while saving file: {e}")

    def load_from_file(self, filename):
        try:
            if not os.path.isfile(filename):
                print(f"Error: The file '{filename}' does not exist.")
                return

            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            if not lines:
                print(f"Error: File '{filename}' is empty.")
                return

            if lines[0].strip().upper() != "TITLE,AUTHOR,PRICE":
                print(f"Error: File '{filename}' has an invalid format.")
                return

            self.Books.clear()

            for lineno, line in enumerate(lines[1:], start=2):
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
            print(f"Inventory loaded successfully from '{filename}'.")
        except PermissionError:
            print(f"Error: Permission denied when trying to read '{filename}'.")
        except FileNotFoundError:
            print(f"Error: The specified file '{filename}' was not found.")
        except OSError as e:
            print(f"Error: OS error occurred: {e}")
        except Exception as e:
            print(f"Unexpected error while loading file: {e}")
