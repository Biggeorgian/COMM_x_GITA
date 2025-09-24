import unittest

class BankAccount:
    def __init__(self, balance, owner):
        self.__balance = balance
        self.__owner = owner

    def deposit(self, amount):
        self.__balance += amount
        return (f"თქვენ ბალანსზე დაირიცხა {amount} ლარი")

    def withdraw(self, amount):
        if self.__balance <= 0:
            return (f"ანგარიშზე თანხა არ არის!")
        elif self.__balance < amount:
            return (f"არასაკმარისი თანხა. "
                  f"შესაძლებელია მხოლოდ {self.__balance} ლარის გატანა")
        elif 0 < amount <= self.__balance:
            self.__balance -= amount
            return (f"ბალანსი: {self.__balance} ლარი")
        else:
            return ("გთხოვთ შეიყვანოთ მხოლოდ დადებითი რიცხვები")

    def get_balance(self):
        return self.__owner, self.__balance

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.atm = BankAccount(100, "Giorgi Goderdzishvili")

    def test_deposit(self):
        result = self.atm.deposit(85)
        self.assertEqual(result, "თქვენ ბალანსზე დაირიცხა 85 ლარი")

    def test_withdraw1000(self):
        result = self.atm.withdraw(1000)
        self.assertEqual(result, "არასაკმარისი თანხა. "
                                 "შესაძლებელია მხოლოდ 100 ლარის გატანა")

    def test_withdraw_negative(self):
        result = self.atm.withdraw(-20)
        self.assertEqual(result, "გთხოვთ შეიყვანოთ მხოლოდ დადებითი რიცხვები")