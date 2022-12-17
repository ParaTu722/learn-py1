import sys
import pygame

from settings import Settings
from ship import Ship


class BlueSky:
    """蓝色天空"""
    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))   # 注意括号

        pygame.display.set_caption("BlueSky")
        self.ship = Ship(self)

    def run_blue_sky(self):
        """开始游戏的主循环"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 每次循环时都重绘屏幕。
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == '__main__':
    ai = BlueSky()
    ai.run_blue_sky()

