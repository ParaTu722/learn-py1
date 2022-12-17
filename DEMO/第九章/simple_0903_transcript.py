class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        # Python将创建一个名为odometer_reading 的属性，并将其初始值设置为0

    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值。"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("\tYou can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量。"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("\t禁止增量为负值")


# 定义一个名为Battery 的新类，它没有继承任何类
class Battery:
    """一次模拟电动汽车电瓶的简单尝试。"""
    def __init__(self, battery_size=75):
        # 另一个形参battery_size 。这个形参是可选的：如果没有给它提供值，电瓶容量将被设置为75
        """初始化电瓶的属性。"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程。"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """检查电瓶容量"""
        if self.battery_size != 100:
            self.battery_size = 100


class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性。再初始化电动汽车特有的属性。"""
        super().__init__(make, model, year)
        # 添加了一个名为self.battery 的属性
        # 这行代码让Python创建一个新的Battery 实例
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()