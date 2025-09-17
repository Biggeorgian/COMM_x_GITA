class BankAccount:
    def __init__(self, balance, owner):
        self.__balance = balance
        self.__owner = owner

    def deposit(self, amount):
        self.__balance += amount
        print(f"თქვენ ბალანსზე დაირიცხა {amount} ლარი.")

    def withdraw(self, amount):
        if self.__balance <= 0:
            print(f"ანგარიშზე თანხა არ არის!")
        elif self.__balance < amount:
            print(f"არასაკმარისი თანხა. "
                  f"შესაძლებელია მხოლოდ {self.__balance} ლარის გატანა")
        elif 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"ბალანსი: {self.__balance} ლარი")
        else:
            print("გთხოვთ შეიყვანოთ მხოლოდ დადებითი რიცხვები")

    def get_balance(self):
        return self.__owner, self.__balance

client = BankAccount(100, "Giorgi Goderdzishvili")

client.deposit(85)
print(f"ანგარიშის მფლობელი {client.get_balance()[0]}. "
      f"ბალანსი: {client.get_balance()[1]}")
client.withdraw(105)
client.withdraw(125)
client.withdraw(80)