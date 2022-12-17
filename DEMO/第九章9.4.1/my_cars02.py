# 9.4.4 导入整个模块
import car


# 9.4.5 导入模块中的所有类
# from module_name import *


my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
