class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置。"""

        # 屏幕设置
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (230, 240, 230)

        # 飞船设置
        self.ship_speed = 1.0
        self.ship_limit = 3     # 玩家拥有的飞船数

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 4     # 存储最大子弹数

        # 外星人设置
        self.alien_speed = 0.1
        self.fleet_drop_speed = 10  # 有外星人撞到屏幕边缘时，外星人群向下移动的速度
        # fleet_direction为1表示向右移，为-1表示向左移。
        self.fleet_direction = 1

        self.speedup_scale = 1.1
        # 外星人分数的提高速度。
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置。"""
        self.ship_speed = 1
        self.bullet_speed = 1.5
        self.alien_speed = 0.2
        # fleet_direction为1表示向右，为-1表示向左。
        self.fleet_direction = 1
        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
