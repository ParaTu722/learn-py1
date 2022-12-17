class Employee:
    """"""

    def __init__(self, first_name, lat_name, salary):
        self.first_name = first_name
        self.lat_name = lat_name
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount
        # print(f"hi, {self.first_name}{self.lat_name} 你的薪水是{self.salary}")
