class ShopingCart():
    def __init__(self, items):
        self.__items = items

    def __len__(self):
        return len(self.__items)

    def __eq__(self, other):
        if not isinstance(other, ShopingCart):
            return False
        return len(self) == len(other)

customer1 = ShopingCart(["ვაშლი", "ბანანი", "ლეღვი", "ატამი"])
customer2 = ShopingCart(["მარწყვი", "რძე", "შაქარი"])
customer3 = ShopingCart(["ანანასი", "შამპანური", "შოკოლადი", "ნამცხვარი"])
customer4 = ShopingCart(["ლუდი", "სოსისი", "მდოგვი", "შებოლილი თევზი", "შავი პური"])

print(f"შევადაროთ პირველი და მეორე მომხმარებლის კალათა: {customer1 == customer2}")
print(f"შევადაროთ პირველი და მესამე მომხმარებლის კალათა: {customer1 == customer3}")
print(f"შევადაროთ პირველი და მეოთხე მომხმარებლის კალათა: {customer1 == customer4}")