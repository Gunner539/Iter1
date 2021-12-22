from collections.abc import Iterable

nested_list = [
    ['a', 'b', 'c', ['11', '22', ['33', '44', ['13', '1a']]]],
    ['d', 'e', 'f'],
    [1, 2, None],
    'aer'
]


def get_flat_list(nested_list, flat_list):
    for el in nested_list:
        if isinstance(el, Iterable) and type(el) != str:
            get_flat_list(el, flat_list)
        else:
            flat_list.append(el)

    return flat_list


class FlatIterator:
    def __init__(self, nested_list):
        self.start = -1
        self.flat_list = get_flat_list(nested_list, [])
        self.end = len(self.flat_list)
        # print('+++')
        # print(self.flat_list)
        # print('---')

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1

        if self.start == self.end:
            raise StopIteration
        else:
            return self.flat_list[self.start]


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
