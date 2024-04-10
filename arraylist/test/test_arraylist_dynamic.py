import unittest
from arraylist.arraylist_dynamic import DynamicList


class TestDynamicList(unittest.TestCase):

    @staticmethod
    def create_default_arraylist():
        arr = DynamicList()
        return arr

    @staticmethod
    def create_test_arraylist_with_data(capacity, size):
        arr = DynamicList(capacity=capacity)
        for _ in range(size):
            arr[_] = (_ + 1) * 7
        return arr

    @staticmethod
    def get_length(arrlist: DynamicList):
        count_not_none = sum(1 for element in arrlist.array if element is not None)
        return count_not_none

    #  Creating a default ArrayList and test its size(0) and capacity(10).
    def test_default_dynamic_arr_list(self):
        darr = self.create_default_arraylist()
        self.assertEqual(len(darr), 0)
        self.assertEqual(darr.array, [None] * 10)

    #  Creating a dynamic ArrayList of given capacity and test it capacity.
    def test_create_dynamic_arr_list(self):
        capacity = 15
        darr = DynamicList(capacity=capacity)
        self.assertEqual(len(darr), 0)
        self.assertEqual(darr.array, [None] * capacity)

    def test_create_dynamic_arr_list_size(self):
        capacity = 15
        size = 7
        darr = DynamicList(capacity=capacity)
        for _ in range(size):
            darr._array[_] = (_+4)*5
        print(darr.array)
        self.assertEqual(self.get_length(darr), size)
        self.assertEqual(len(darr.array), capacity)
        self.assertEqual(darr.array, [20, 25, 30, 35, 40, 45, 50, None, None, None, None, None, None, None, None])


if __name__ == '__main__':
    unittest.main()
