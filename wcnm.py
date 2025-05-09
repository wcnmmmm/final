from final import books

b = books()

v = input("Would you like to add a book? (yes/no): ").strip().lower()
if v == "yes":
    b.add()

v = input("Show all books? (yes/no): ").strip().lower()
if v == "yes":
    b.show()

v = input("Would you like to sell a book? (yes/no): ").strip().lower()
if v == "yes":
    b.sell()

v = input("Save inventory to file? (yes/no): ").strip().lower()
if v == "yes":
    fname = input("Enter filename to save (e.g. books.txt): ").strip()
    b.save_to_file(fname)

v = input("Load inventory from file? (yes/no): ").strip().lower()
if v == "yes":
    fname = input("Enter filename to load (e.g. books.txt): ").strip()
    b.load_from_file(fname)