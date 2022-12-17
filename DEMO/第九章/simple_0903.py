# 9.3 继承
# 9.3.1 子类的方法__init__()

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

    def fill_gas_tank(self):
        """汽车有油箱。"""
        print("This car need a gas tank!")
# 父类如上Car,创建子类时，父类必须包含在当前文件中，且位于子类前面


# 定义子类时，必须在圆括号内指定父类的名称
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性。"""
        super().__init__(make, model, year)
        # 父类也称为超类 ，名称super 由此而来
        self.battery_size = 75      # 电动汽车特有的属性（电瓶）

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size} -kWh battery.")

    def fill_gas_tank(self):
        """电动汽车没有油箱。"""
        print("This car doesn't need a gas tank!")


my_car = ElectricCar('tesla', 'model s', 2019)
print(my_car.get_descriptive_name())


# 9.3.2 给子类定义属性和方法
# 第45，47行
my_car.describe_battery()

# 9.3.3 重写父类的方法
# my_car.fill_gas_tank()      # 经过重写后调用 ，第55行
# 这样，Python将不会考虑这个父类方法，而只关注你在子类中定义的相应方法。
my_car.fill_gas_tank()

# 9.3.4 将实例用作属性 ， 见simple_0903_transcript.py

# 9.3.5 模拟实物


print('\n------------------------------\n')


# 练习9-6：冰激凌小店
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性name和age"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, count):
        """设置就餐人数"""
        self.number_served = count
        print(f"吃饭的有{self.number_served}人")

    def increment_number_served(self, add_count):
        """将就餐人数递增"""
        self.number_served += add_count
        print(f"现在吃饭的有{self.number_served}人")


class IceCreamStand(Restaurant):
    """冰激凌小店是一种特殊的餐馆,继承练习9-4"""
    def __int__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []   # 定义空列表，在119行手动赋值

    def show_flavors(self):
        """显示这些冰激凌的方法"""
        print("\nWe have the following flavors available:")
        # 遍历列表
        for flavor in self.flavors:
            print(f"\t{flavor}口味的冰淇淋")


iceCreamStand_simple = IceCreamStand('冰激凌小店', '冰激凌')
print(f"我在{iceCreamStand_simple.restaurant_name}吃{iceCreamStand_simple.cuisine_type}")
iceCreamStand_simple.set_number_served(5)

iceCreamStand_simple.flavors = ['草莓', '西瓜', '葡萄']

iceCreamStand_simple.show_flavors()


print('\n------------------------------\n')


# 练习9-7：管理员 　
class User:
    def __init__(self, first_name, last_name, age):
        """初始化属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """信息创建"""
        print(f"Ta的全名是{self.first_name}{self.last_name},今年{self.age}")

    def greet_user(self):
        """问候语"""
        print('happy days\n')

    def increment_login_attempts(self):
        """登录+1"""
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        """登录置0"""
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, age):
        """继承父类属性"""
        super().__init__(first_name, last_name, age)
        # super().__init__(first_name, last_name, age)格式不能错！！！
        # self.privileges = []
        self.privileges = Privileges()    # 格式！！！将一个Privileges实例用作其属性
"""
    def show_privileges(self):
        for privilege in self.privileges:
            print(f"\t管理员的权限:{privilege}")


admin = Admin('王', '五', 16)
admin.describe_user()
admin.privileges = ['can add post', 'can ban user', 'candelete post']
admin.show_privileges()
"""

print('\n------------------------------\n')


# 练习9-8：权限 　
# 要注释掉上面的show_privileges方法
class Privileges:
    def __init__(self):
        self.privileges_02 = ['can add post', 'can ban user', 'candelete post']

    def show_privileges(self):
        for privilege in self.privileges_02:
            print(f"\t管理员的权限:{privilege}")


admin = Admin('王', '五', 16)
admin.describe_user()
admin.privileges.show_privileges()


# 练习9-9：电瓶升级
