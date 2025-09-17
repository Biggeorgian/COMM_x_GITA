class CustomList:
    def __init__(self, input_data):
        self.data = list(input_data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __iter__(self):
        return iter(self.data)

list1 = CustomList(["a", "b", "c", "d", "e", "f"])
print("საწყისი სია")
for index, item in enumerate(list1):
    print(f"{index + 1}: {item}")

print("შევცვალეთ 2 ინდექსის მნიშვნელობა")
list1[2] = "rr"
for index, item in enumerate(list1):
    print(f"{index + 1}: {item}")