class CyclicIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            return next(self.iterator)


if __name__ == "__main__":
    try:

        # тесты
        cyclic_iterator = CyclicIterator(range(3))
        for i in cyclic_iterator:
            print(i)
        #
        # list = [2,3,4,5]
        # cyclic_iterator = CyclicIterator(list)
        # for i in cyclic_iterator:
        #     print(i)


    # a = tuple('hello, world!')
    # cyclic_iterator = CyclicIterator(a)
    # for i in cyclic_iterator:
    #     print(i)

    # d = dict(short='dict', long='dictionary')
    # cyclic_iterator = CyclicIterator(d)
    # for i in cyclic_iterator:
    #      print(i)

    except KeyboardInterrupt:
        print('\nBye-bye')
