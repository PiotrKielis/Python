from collections.abc import Sequence


class SortedList(Sequence):
    def __init__(self, iterable=None, key=None):
        self._items = []
        self._key = key
        if iterable is not None:
            for item in iterable:
                self.add(item)

    @property
    def key(self):
        return self._key

    def clear(self):
        self._items.clear()

    def _find_index(self, value):
        """Metoda chroniona (protected), zwraca indeks miejsca, w które należy
        wstawić dany element, korzystając z algorytmu wyszukiwania binarnego."""
        lo, hi = 0, len(self._items)
        while lo < hi:
            mid = (lo + hi) // 2
            if self._items[mid] < value:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def add(self, value):
        """Dodaje element do listy w odpowiednim miejscu, aby lista pozostała posortowana."""
        index = self._find_index(value)
        self._items.insert(index, value)

    def pop(self, index=-1):
        """Usuwa i zwraca element o podanym indeksie (domyślnie ostatni)."""
        return self._items.pop(index)

    def remove(self, value):
        """Usuwa pierwszy element o podanej wartości."""
        self._items.remove(value)

    def remove_every(self, value):
        """Usuwa wszystkie elementy o podanej wartości."""
        while value in self._items:
            self._items.remove(value)

    def __delitem__(self, index):
        """Usuwa element o podanym indeksie."""
        del self._items[index]

    def __getitem__(self, index):
        """Zwraca element o podanym indeksie."""
        return self._items[index]

    def __setitem__(self, index, value):
        """Ustawia element o podanym indeksie na podaną wartość."""
        self._items[index] = value

    def __len__(self):
        """Zwraca liczbę elementów w liście."""
        return len(self._items)

    def __str__(self):
        """Zwraca stringową reprezentację listy."""
        return str(self._items)

    def copy(self):
        """Zwraca kopię listy."""
        return SortedList(self._items, key=self._key)

    def __copy__(self):
        """Zwraca kopię listy."""
        return self.copy()

    def extend(self, iterable):
        """Rozszerza listę o elementy z iterable."""
        for item in iterable:
            self.add(item)

    def count(self, value):
        """Zwraca liczbę wystąpień podanej wartości."""
        return self._items.count(value)

    def index(self, value, start=0, stop=None):
        """Zwraca indeks pierwszego elementu o podanej wartości."""
        if start is None:
            start = 0
        if stop is None:
            stop = len(self._items)
        return self._items.index(value, int(start), int(stop))

    def __contains__(self, value):
        """Zwraca True, jeśli podana wartość jest w liście."""
        return value in self._items

    def __iter__(self):
        """Zwraca iterator po elementach listy."""
        return iter(self._items)

    def __reversed__(self):
        """Zwraca odwrócony iterator po elementach listy."""
        return reversed(self._items)


s = SortedList([3, 1, 4, 1, 5, 9, 2, 6, 5])
print(list(s))  # powinno wypisać: [1, 1, 2, 3, 4, 5, 5, 6, 9]

s.add(7)
print(list(s))  # powinno wypisać: [1, 1, 2, 3, 4, 5, 5, 6, 7, 9]

s.remove(1)
print(list(s))  # powinno wypisać: [1, 2, 3, 4, 5, 5, 6, 7, 9]

s.remove_every(5)
print(list(s))  # powinno wypisać: [1, 2, 3, 4, 6, 7, 9]

print(len(s))  # powinno wypisać: 7

print(2 in s)  # powinno wypisać: True
print(5 in s)  # powinno wypisać: False

print(s.index(6))  # powinno wypisać: 4

t = s.copy()
t.add(8)
print(list(s))  # powinno wypisać: [1, 2, 3, 4, 6, 7, 9]
print(list(t))  # powinno wypisać: [1, 2, 3, 4, 6, 7, 8, 9]
