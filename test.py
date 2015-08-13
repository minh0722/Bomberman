import unittest

from object import Object


class TestObject(unittest.TestCase):
    def test_object_position(self):
        object = Object((0, 22), 10, 20)

        self.assertEqual(object.position(), (0,22))

    def test_object_width(self):
        object = Object((12, 23), 5, 8)

        self.assertEqual(object.get_width(), 5)

    def test_object_height(self):
        object = Object((88, 54), 345, 334)

        self.assertEqual(object.get_height(), 334)

    def test_object_get_x(self):
        object = Object((122, 45), 47, 33)

        self.assertEqual(object.get_x(), 122)

    def test_object_get_y(self):
        object = Object((876, 123), 65, 6)

        self.assertEqual(object.get_y(), 123)

    def test_move_left(self):
        object = Object((100, 100), 43, 33)

        object.move_left(5)

        self.assertEqual(object.get_x(), 95)

    def test_move_right(self):
        object = Object((443, 1123), 65, 498)

        object.move_right(10)

        self.assertEqual(object.get_x(), 453)

if __name__ == "__main__":
    unittest.main()