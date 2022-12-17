# 9.2 使用类和实例

class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # 用于读取汽车的里程表
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


my_newcar = Car('audi', 'a4', 2019)
print(my_newcar.get_descriptive_name())
my_newcar.read_odometer()

print('-----------------------------------------')
print('-----------------------------------------')

# 9.2.3 修改属性的值

# 第一种:直接修改属性的值
my_newcar.odometer_reading = 234
my_newcar.read_odometer()

print('-----------------------------------------')
print('-----------------------------------------')

# 第二种:通过方法修改属性的值,见25行
# 还可对方法update_odometer() 进行扩展,见24行

my_newcar.update_odometer(789)
my_newcar.read_odometer()

print('-----------------------------------------')

my_newcar.update_odometer(89)
my_newcar.read_odometer()

print('-----------------------------------------')
print('-----------------------------------------')


# 第三种:通过方法对属性的值进行递增
# 新增的方法increment_odometer()，第29行
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(2345)
my_used_car.read_odometer()

my_used_car.increment_odometer(258)
my_used_car.read_odometer()
my_used_car.increment_odometer(-100)
my_used_car.read_odometer()


print('-----------------------------------------')
print('-----------------------------------------')


# 练习9-4：就餐人数
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性name和age"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def open_restaurant(self):
        """开业描述"""
        print("餐馆正在营业。")

    def set_number_served(self, count):
        """设置就餐人数"""
        self.number_served = count
        print(f"吃饭的有{self.number_served}人")

    def increment_number_served(self, add_count):
        """将就餐人数递增"""
        self.number_served += add_count
        print(f"现在吃饭的有{self.number_served}人")


restaurant = Restaurant('饺子馆', '猪肉大葱馅')
print(f"{restaurant.restaurant_name}卖{restaurant.cuisine_type}")
restaurant.open_restaurant()
restaurant.set_number_served(12)
restaurant.increment_number_served(22)

print('-----------------------------------------')
print('-----------------------------------------')


# 练习9-5：尝试登录次数
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


user = User('王', '五', 16)
user.describe_user()
print(f"初始的登录次数为{user.login_attempts}")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"现在的登录次数为{user.login_attempts}")
user.reset_login_attempts()
print(f"现在的登录次数为{user.login_attempts}")





