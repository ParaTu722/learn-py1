# 11.1.1 单元测试和测试用例
"""
Python标准库中的模块unittest 提供了代码测试工具。
单元测试: 用于核实函数的某个方面没有问题
测试用例: 是一组单元测试，它们一道核实函数在各种情形下的行为都符合要求。
全覆盖: 的测试用例包含一整套单元测试，涵盖了各种可能的函数使用方式。
"""

import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    # 这个类必须继承unittest.TestCase类，这样Python才知道如何运行你编写的测试
    """测试name_function.py。"""
    def test_first_last_name_01(self):
        formatted_name = get_formatted_name('janis', 'joplin', middle='kkk')
        self.assertEqual(formatted_name, 'Janis Kkk Joplin')
        # 断言方法:断言方法核实得到的结果是否与期望的结果一致

    def test_first_last_name_02(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_name_03(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()
# 11.1.2 可通过的测试
"""
Ran 1 test in 0.001s

OK
"""


# 11.1.3 未通过的测试
# 18行数据格式与所测试的函数里的不一样是，有报错

# 11.1.4 测试未通过时怎么办
