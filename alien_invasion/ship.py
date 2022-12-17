import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置。"""
        super().__init__()
        # 将屏幕赋给了Ship 的一个属性，以便在这个类的所有方法中轻松访问
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # 用方法get_rect()访问屏幕的属性rect,并将其赋给了self.screen_rect
        self.screen_rect = ai_game.screen.get_rect()    #（rect 对象）

        # 加载飞船图像并获取其外接矩形。
        self.image = pygame.image.load('images/ship.bmp')
        # 使用get_rect() 获取相应surface的属性rect ，以便后面能够使用它来指定飞船的位置
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕底部的中央。
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性x中存储小数值。
        self.x = float(self.rect.x)
        # 移动标志。
        self.moving_left = False
        self.moving_right = False

    def blitme(self):
        """在指定位置绘制飞船。"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞船的位置。"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.right 返回飞船外接矩形右边缘的x坐标。如果这个值小于self.screen_rect.right的值则未触及右边缘
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # 根据self.x更新rect对象。
        self.rect.x = self.x

    def center_ship(self):
        """让飞船在屏幕底端居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
