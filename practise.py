a = [
    ("Shreejan","Srestha"),
    ("Shristi", "Shakya"),
    ("Sunil","Phoju"),
    ("Srijan","Basnet"),
    ("Shreejan","DOn")
]

d = {}
for name, cast in a:
    if name in d:
        d[name].append(cast)
    else:
        d[name] =[cast]
# print(d)

print(ord('a'))
