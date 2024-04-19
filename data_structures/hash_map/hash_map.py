# https://github.com/donnemartin/system-design-primer/blob/master/solutions/object_oriented_design/hash_table/hash_map.ipynb

class Item(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]


if __name__ == '__main__':
    table = [[] for _ in range(5)]
    print(table)