
from final import books

b = books()

print(b.name)

v = input("Would you like to add a book? (yes/no): ").strip().lower()
if v == "yes":
    b.Add()
elif v == "no":
    b.sell()
else:
    print("Invalid choice, skipping add/sell step.")

v = input("Show all books? (yes/no): ").strip().lower()
if v == "yes":
    b.showbook()

v = input("Save inventory to file? (yes/no): ").strip().lower()
if v == "yes":
    fname = input("Enter filename (e.g. books.json): ").strip()
    b.save_to_file(fname)

v = input("Load inventory from file? (yes/no): ").strip().lower()
if v == "yes":
    fname = input("Enter filename (e.g. books.json): ").strip()
    b.load_from_file(fname)