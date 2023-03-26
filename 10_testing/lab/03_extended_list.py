class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTest(TestCase):
    def test_is_initialed_correctly_without_data(self):
        my_int = IntegerList()
        self.assertEqual([], my_int._IntegerList__data)

    def test_is_initialed_correctly_with_correct_data(self):
        my_int = IntegerList(1,2,3,4)
        self.assertEqual([1, 2, 3, 4], my_int._IntegerList__data)

    def test_is_initialed_correctly_wit_wrong_data(self):
        my_int = IntegerList("a", "b", 4.5, 2.5)
        self.assertEqual([], my_int._IntegerList__data)

    def test_get_data(self):
        my_int = IntegerList(1, 2)
        self.assertEqual([1, 2], my_int._IntegerList__data)

        my_int.get_data()
        self.assertEqual([1, 2], my_int._IntegerList__data)

    def test_add_wrong_element_exception(self):
        my_int = IntegerList(1, 2)
        self.assertEqual([1, 2], my_int._IntegerList__data)

        with self.assertRaises(ValueError) as ex:
            my_int.add("asd")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_correct_element_exception(self):
        my_int = IntegerList(1, 2)
        self.assertEqual([1, 2], my_int._IntegerList__data)

        my_int.add(5)
        self.assertEqual([1, 2, 5], my_int._IntegerList__data)

    def test_remove_index_out_of_range(self):
        my_int = IntegerList(1, 2)
        self.assertEqual([1, 2], my_int._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            my_int.remove_index(2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_el_removes_the_el(self):
        my_int = IntegerList(1, 2)
        self.assertEqual([1, 2], my_int._IntegerList__data)

        my_int.remove_index(1)
        self.assertEqual([1], my_int._IntegerList__data)

    def test_remove_return_result(self):
        my_int = IntegerList(1, 2)
        self.assertEqual([1, 2], my_int._IntegerList__data)

        x = my_int.remove_index(1)
        self.assertEqual(2, x)

    def test_get_index_is_out_of_range(self):
        my_int = IntegerList(1, 2)
        self.assertEqual([1, 2], my_int._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            my_int.get(2)
        self.assertEqual("Index is out of range", str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            my_int.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_valid_index(self):
        my_int = IntegerList(1, 2)
        self.assertEqual([1, 2], my_int._IntegerList__data)

        x = my_int.get(1)
        self.assertEqual(2, x)

    def test_insert_correct_data_with_invalid_index(self):
        my_int = IntegerList(1, 2)
        self.assertEqual([1, 2], my_int._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            my_int.insert(2, 2)
        self.assertEqual("Index is out of range", str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            my_int.insert(3, 2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_incorrect_data_with_valid_index(self):
        my_int = IntegerList(1, 2)
        self.assertEqual([1, 2], my_int._IntegerList__data)

        with self.assertRaises(ValueError) as ex:
            my_int.insert(1, "2")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_elements(self):
        my_int = IntegerList(1, 2)
        self.assertEqual([1, 2], my_int._IntegerList__data)

        my_int.insert(1, 3)
        self.assertEqual([1, 3, 2], my_int._IntegerList__data)

    def test_get_biggest(self):
        my_int = IntegerList(1, 2, 3, 8, 5, 6, 7, -2)

        result = my_int.get_biggest()
        self.assertEqual(8, result,)

    def test_get_index(self):
        my_int = IntegerList(1, 2)

        result = my_int.get_index(2)
        self.assertEqual(1, result)

if __name__ == '__main__':
    main()