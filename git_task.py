shops = {
    "x.com": ["kolejny monitor", "wieszak na monitor", "jeszcze jeden monitor"],
    "ikea": ["nowe biureczko", "szafa", "wygodniejsze krzesło", "dywanik pod stopy"]
}

length = 0
for shop in shops.keys():
    items = shops[shop]
    items = [item.capitalize() for item in items]
    length = length + len(items)
    print(f"I go to {shop.capitalize()} and buy some {items}")
    

print(f"W sumie jest {length} rzeczy")
