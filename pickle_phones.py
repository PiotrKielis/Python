import pickle

class Smartphone:
    def __init__(self, manufucturer, model, price):
        self.__manufucturer = manufucturer
        self.__model = model
        self.__price = price

    def set_manfucturer(self, manufucturer):
        self.__manufucturer = manufucturer

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        self.__price = price

    def get_manufucturer(self):
        return self.__manufucturer

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"{self.__manufucturer} {self.__model}, {self.__price}"

def save_phones_to_file(filename, phones):
    with open(filename, 'wb') as f:
        pickle.dump(phones, f)

def read_phones_from_file(filename):
    with open(filename, 'rb') as f:
        phones = pickle.load(f)
    return phones

if __name__ == "__main__":
    phones = [
        Smartphone("Samsung", "Galaxy S21", 3500),
        Smartphone("Apple","Iphone 12", 4200),
        Smartphone("Xiaomi", "Redmi Note 10", 1200)
    ]

    save_phones_to_file("phones.dat", phones)

    phones_loaded = read_phones_from_file("phones.dat")
    for phone in phones_loaded:
        print(phone)
