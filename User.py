class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print("User:" + self.name, "Balance:" + self.account_balance)

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

# Create three instances of class

eren = User("Eren Yeager", "eren.yeager@titan.com")
mikasa = User("Mikasa Ackerman", "mikasa.ackerman@titan.com")
reiner = User("Reiner Braun", "reiner.braun@titan.com")

# First user make 3 deposits and one withdrawal and display the balance

eren.make_deposit(10)
eren.make_deposit(600)
eren.make_deposit(40)
eren.make_withdrawal(50)

print("User:", str(eren.name + ","), "Balance:", eren.account_balance)

# Second user makes 2 deposits and 2 withdrawals and display the balance

mikasa.make_deposit(100)
mikasa.make_deposit(200)
mikasa.make_withdrawal(50)
mikasa.make_withdrawal(10)

print("User:", str(mikasa.name + ","), "Balance:", mikasa.account_balance)

# Third user makes 1 deposit and 3 withdrawals and display the balance

reiner.make_deposit(500)
reiner.make_withdrawal(15)
reiner.make_withdrawal(25)
reiner.make_withdrawal(60)

print("User:", str(reiner.name + ","), "Balance:", reiner.account_balance)

# Have the first user transfer money to the third user and then print both users' balances

eren.transfer_money(reiner, 200)

print("User:", str(eren.name + ","), "Balance:", eren.account_balance)
print("User:", str(reiner.name + ","), "Balance:", reiner.account_balance)
