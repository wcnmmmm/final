from final import books
b=books()
print(b.name)

v=input("would you like to add a book (yes/no)")
if v== "yes":
    c=b.Add()
if v=="no":
    c=b.minus()
v = input("Show all books? (yes/no): ").strip().lower()
if v == "yes":
    b.showbook()
v = input("Save inventory to file? (yes/no): ").strip().lower()
if v == "yes":
    fname = input("Enter filename (e.g. books.json): ").strip()
    b.save_to_file(fname)