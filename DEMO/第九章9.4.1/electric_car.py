"""一组可用于表示电动汽车的类。"""

# 接将Car 类导入该模块中
from car import Car

"""
class Battery:
    --snip--
    
class ElectricCar(Car):
    --snip--


"""

# 用 from electric_car import ElectricCar 在别的文件中调用


# 9.4.7 使用别名
# from electric_car import ElectricCar as EC

# 调用 my_tesla = EC('tesla', 'roadster', 2019)