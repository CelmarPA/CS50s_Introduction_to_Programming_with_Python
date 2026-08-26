class Jar:

    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n < 0:
            raise ValueError()

        self.size += n

    def withdraw(self, n):
        if n < 0 or n > self.size:
            raise ValueError()

        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError()

        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        if n < 0:
            raise ValueError()

        if n > self.capacity:
            raise ValueError()

        self._size = n


def main():
    jar = Jar()
    jar.deposit(10)
    print(jar)
    jar.withdraw(5)
    print(jar)
    print(jar.size)
    print(jar.capacity)


if __name__ == "__main__":
    main()
