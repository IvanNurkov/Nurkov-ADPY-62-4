class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.iter_counter = -1
        self.len_ = len(list_of_list)


    def __iter__(self):
        self.iter_counter += 1
        self.iter_cursor = 0
        return self

    def __next__(self):
        while self.iter_counter - self.len_ and self.iter_cursor == len(self.list_of_list[self.iter_counter]):
            iter(self)
        if self.iter_counter == self.len_:
            raise StopIteration
        self.iter_cursor += 1
        return self.list_of_list[self.iter_counter][self.iter_cursor - 1]


def test_1():


    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    flat_list = [item for item in FlatIterator(list_of_lists_1)]
    print(flat_list)


if __name__ == '__main__':
    test_1()





import types


def flat_generator(list_of_lists):
    for list_1 in list_of_lists:
        for list_2 in list_1:
            yield list_2



def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    ready_list = []

    for item in flat_generator(list_of_lists_1):
        ready_list.append(item)
    print(ready_list)



if __name__ == '__main__':
    test_2()
