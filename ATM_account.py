class Account:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def pay(self, amount):
        self.__balance += amount

    def take(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Brak środków na koncie")

    def __str__(self):
        return f"Saldo konta: {self.__balance}"


def main():
    initial_balance = float(input("Podaj początkowe saldo konta: "))
    account = Account(initial_balance)

    while True:
        print("\nCo chcesz zrobić?")
        print("1. Wpłać pieniądze")
        print("2. Wypłać pieniądze")
        print("3. Sprawdź stan konta")
        print("4. Zakończ program")

        choice = input("Wybierz opcję: ")
        if choice == "1":
            amount = float(input("Podaj kwotę do wpłaty: "))
            account.pay(amount)
            print(f"Wpłaciłeś {amount} zł. Aktualne saldo konta to: {account}")
        elif choice == "2":
            amount = float(input("Podaj kwotę do wypłaty: "))
            account.take(amount)
            print(f"Wypłaciłeś {amount} zł. Aktualne saldo konta to: {account}")
        elif choice == "3":
            print(f"Aktualne saldo konta to: {account}")
        elif choice == "4":
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")


if __name__ == "__main__":
    main()
