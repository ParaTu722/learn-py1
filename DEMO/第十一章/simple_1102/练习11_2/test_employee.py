import unittest
from employee import Employee

class Test_employee(unittest.TestCase):
    """测试模块 employee。"""
    def setUp(self):
        self.eric = Employee('eric', 'matthes', 65_000)

    def test_give_default_raise(self):
        self.eric.give_raise()
        self.assertEqual(self.eric.salary, 70_000)

    def test_give_custom_raise(self):
        """测试自定义年薪增加量是否可行。"""
        self.eric.give_raise(10_000)
        self.assertEqual(self.eric.salary, 75_000)


if __name__ == '__main__':
    unittest.main()