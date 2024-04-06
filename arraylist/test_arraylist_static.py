import unittest

from arraylist.arraylist_static import ArrayList


class TestArrayList(unittest.TestCase):

    @staticmethod
    def create_test_arraylist(size):
        arr = ArrayList(size)
        return arr

    @staticmethod
    def create_test_arraylist_with_data(size):
        arr = ArrayList(size)
        for _ in range(size):
            arr[_] = (_ + 1) * 7
        return arr

    #  Creating an ArrayList object with a positive integer size initializes an empty list of that size.
    def test_create_arraylist_positive_size(self):
        size = 5
        arr = self.create_test_arraylist(size)
        self.assertEqual(len(arr), size)
        self.assertEqual(arr.data, [None] * size)

    #  The __getitem__ method returns the element at the specified index.
    def test_getitem(self):
        arr = self.create_test_arraylist_with_data(5)
        for _ in range(len(arr)):
            self.assertEqual(arr.__getitem__(_), (_ + 1) * 7)

    #  The __setitem__ method sets the element at the specified index to the specified value.
    def test_setitem(self):
        arr = self.create_test_arraylist(5)
        for _ in range(len(arr)):
            arr.__setitem__(_, (_+1)*10)
            self.assertEqual(arr[_], (_+1)*10)

    #  The __len__ method returns the size of the ArrayList.
    def test_len(self):
        arr = self.create_test_arraylist(5)
        self.assertEqual(arr.__len__(), 5)

    def test_len_method(self):
        arr = self.create_test_arraylist(5)
        self.assertEqual(len(arr), 5)

    #  The add_element method is used to add the same type elements to the ArrayList.
    def test_add_element_same_type(self):
        arr = self.create_test_arraylist(5)
        arr.add_element(10)
        arr.add_element(12)
        arr.add_element(15)
        self.assertEqual(arr.data, [10, 12, 15, None, None])

    def test_add_element_diff_type(self):
        arr = self.create_test_arraylist(5)
        arr.add_element(10)
        with self.assertRaises(TypeError):
            arr.add_element('sam')
        arr.add_element(15)
        self.assertEqual(arr.data, [10, 15, None, None, None])

    #  Creating an ArrayList object with a size of 0 initializes an empty list.
    def test_create_arraylist_zero_size(self):
        size = 0
        arr = self.create_test_arraylist(size)
        self.assertEqual(len(arr), size)
        self.assertEqual(arr.data, [])

    #  Creating an ArrayList object with a negative integer size raises a ValueError.
    def test_create_arraylist_negative_size(self):
        size = -5
        with self.assertRaises(ValueError):
            self.create_test_arraylist(size)

    #  Accessing an index outside the range of the ArrayList raises an IndexError.
    def test_index_out_of_range(self):
        arr = self.create_test_arraylist(5)
        with self.assertRaises(IndexError):
            arr[5]

    #  Adding an element of a different type than the list type raises a TypeError.
    def test_add_element_different_type(self):
        arr = self.create_test_arraylist(5)
        arr.add_element(10)
        arr.add_element(12)
        with self.assertRaises(TypeError):
            arr.add_element("15")

    #  Creating an ArrayList object with a non-integer size raises a TypeError.
    def test_create_arraylist_non_integer_size(self):
        size = "5"
        with self.assertRaises(TypeError):
            self.create_test_arraylist(size)

    #  Creating an ArrayList object with a large size creates a list of that size.
    def test_create_arraylist_large_size(self):
        size = 1000000
        arr = self.create_test_arraylist(size)
        self.assertEqual(len(arr), size)
        self.assertEqual(arr.data, [None] * size)

    #  Creating an ArrayList object with a size of 1 initializes a list with one element.
    def test_create_arraylist_size_one(self):
        size = 1
        arr = self.create_test_arraylist(size)
        self.assertEqual(len(arr), size)
        self.assertEqual(arr.data, [None])

    def test_list_reverse_method(self):
        arr = ArrayList(5)
        for _ in range(5):
            arr[_] = _+5
        print(arr)
        arr.data.reverse()
        print(arr)
        # self.assertEqual(arr.data, [10, 12, 15, None, None])


if __name__ == '__main__':
    unittest.main()
