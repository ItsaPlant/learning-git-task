shops = {
    "x.com": ["kolejny monitor", "wieszak na monitor", "jeszcze jeden monitor"],
    "ikea": ["nowe biureczko", "duża szafa", "wygodniejsze krzesło", "dywanik pod stopy"]
}

for shop in shops.keys():
    items = shops[shop]

    for item in items:
        item.capitalize()
        print(item)
print(f" I go to {shop} and buy {items}")

txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)