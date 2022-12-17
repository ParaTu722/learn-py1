"""
创建和使用类
"""

# 9.1.1创建dog类
# 在Python中，首字母大写的名称指的是类
class Dog:
    # 类中的函数称为方法
    # 方法__init__() 是一个特殊方法，每当你根据Dog 类创建新实例时，Python都会自动运行它
    # 我们将方法__init__() 定义成包含三个形参：self 、name 和age
    # 形参self 必不可少，而且必须位于其他形参的前面
    def __init__(self, name, age):
        """初始化属性name和age"""
        # 以self 为前缀的变量可供类中的所有方法使用
        self.name = name
        self.age = age

    def sit(self):
        """模式收到坐下命令"""
        print(f"{self.name}正在坐下.")

    def roll_over(self):
        """模式收到打滚命令"""
        print(f"{self.name}正在打滚.")


"""
Python使用实参'bob' 和5 调用Dog 类的方法__init__() 。
方法__init__() 创建一个表示特定小狗的实例，并使用提供的值来设置属性name 和age
"""
my_dog = Dog('bob', 5)
print(f"{my_dog.name}是我的狗，它{my_dog.age}岁了.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Lucy', 3)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

print('\n\n')


# 动手试一试
# 9.1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性name和age"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def open_restaurant(self):
        """开业描述"""
        print("餐馆正在营业。\n")


restaurant = Restaurant('饺子馆', '饺子')
print(f"{restaurant.restaurant_name}卖{restaurant.cuisine_type}")
restaurant.open_restaurant()

restaurant = Restaurant('炒菜馆', '炒饭')
print(f"{restaurant.restaurant_name}卖{restaurant.cuisine_type}")
restaurant.open_restaurant()

restaurant = Restaurant('烧烤店', '烤串')
print(f"{restaurant.restaurant_name}卖{restaurant.cuisine_type}")
restaurant.open_restaurant()


# 9.3
class User:
    def __init__(self, first_name, last_name, age):
        """初始化属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        """信息创建"""
        print(f"Ta的全名是{self.first_name}{self.last_name},今年{self.age}")
    def greet_user(self):
        """问候语"""
        print('{}{},happy days\n'.format(self.first_name, self.last_name))


user01 = User('王', '五', 16)
user01.describe_user()
user01.greet_user()
user02 = User('张', '三', 26)
user02.describe_user()
