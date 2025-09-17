class Refrigerator:
    def __init__(self, products=None):
        if products == None:
            self.products = []
        else:
            self.products = list(products)

    def __contains__(self, item):
        return item in self.products

    def __str__(self):
        num_items = len(self.products)
        item_list = ", ".join(self.products)
        return f"მაცივარში არის {num_items} პროდუქტი: {item_list}"

    def __del__(self):
        print(f"პროდუქტები გადაიყარა...\nახლა მაცივარი გამორთულია")

basket = ["cheese", "butter", "eggs", "milk", "meat", "butter",  ]
fridge = Refrigerator(basket)

print(fridge)

if "milk" in fridge:
    print("✓ დიახ, მაცივარში არის რძე (milk).")
else:
    print("✗ არა, მაცივარში არ არის რძე.")

del fridge