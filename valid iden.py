import keyword

identifiers = ["2value", "value_2", "_hidden", "class", "my-var", "MyClass", "total$"]

for name in identifiers:
    if name.isidentifier() and not keyword.iskeyword(name):
        print(f"{name} -> Valid Identifier")
    else:
        print(f"{name} -> Invalid Identifier")