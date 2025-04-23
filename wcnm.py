from final import books
b=books()
print(b.name)

v=input("would you like to add a book (yes/no)")
if v== "yes":
    c=b.Add()
if v=="no":
    c=b.minus()
