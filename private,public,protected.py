class BankAccount:
    def __init__(self, account_number, account_holder, balance):
          self. account_number = account_number # Public
          self._account_holder = account_holder # Protected
          self.__balance = balance # Private

    def deposit(self, amount):
		    if amount > 0:
 self.__balance += amount
print(f"Deposited ₹{amount}. New Balance: 			₹{self.__balance}")
 else:
			print("Invalid deposit amount.")

# Public Method
def withdraw(self, amount):
		if 0 < amount <= self. __balance:
			self. __balance -= amount
			print(f"Withdrew ₹{amount}. Remaining 				Balance: ₹{self.__balance}")
		else:
			print("Insufficient funds or invalid amount.")


# Protected Method
def _display_holder_info(self):
	print(f"Account Holder: {self._account_holder}")

# Private Method
def __apply_bank_charges(self):

	self.__balance -= 50
	print("₹50 bank charge applied.")

def month_end_process(self):
		self.__apply_bank_charges()
		print("Month-end processing done.")



account = BankAccount("123456", "Muthu", 5000)
