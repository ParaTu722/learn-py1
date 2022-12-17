import unittest     # 别忘了导入模块unittest和要测试的函数
from city_functions import city_country


class TestCityCountry_01(unittest.TestCase):
    """函数进行测试"""
    def test_city_country(self):
        test_cy = city_country('santiago', 'chile')
        self.assertEqual(test_cy, 'Santiago , Chile')

    def test_city_country_population(self):
        test_cy = city_country('santiago', 'chile', population=123456)
        # int类型数字的输入，不能直接写123456，要（变量名=123456）
        self.assertEqual(test_cy, 'Santiago , Chile-population 123456')


if __name__ == '__main__':
    unittest.main()
