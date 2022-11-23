with open("pg3333.txt", "r", encoding="utf-8") as text:
    d = {}
    a = text.read(1)
    while a:
        if a.isalpha():
            a = a.lower()
            d[a] = d.get(a, 0) + 1
        a = text.read(1)


for e in sorted(d,key=lambda e:d[e], reverse=True):
    print(e,d[e])
