import sys
import pygame

from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from random import randint
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button


class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        # 初始化背景设置
        pygame.init()
        # 创建一个Settings 实例并将其赋给self.settings
        self.settings = Settings()

        # pygame.display.set_mode(...)创建一个显示窗口，游戏的所有图形元素都将在其中绘制。
        # 实参(1200, 800) 是一个元组，指定了游戏窗口的尺寸
        # 使用了self.settings 的属性
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        """
        全屏
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        """
        pygame.display.set_caption("Alien Invasion")

        # 创建一个用于存储游戏统计信息的实例。
        self.stats = GameStats(self)
        # 并创建记分牌。
        self.sb = Scoreboard(self)
        # 设置背景颜色RGB(红绿蓝)
        # self.bg_color = (230, 240, 230)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()    # 创建用于存储子弹的编组
        """这个编组是pygame.sprite.Group 类的一个实例。
        pygame.sprite.Group 类似于列表，但提供了有助于开发游戏的额外功能
        在主循环中，将使用这个编组在屏幕上绘制子弹以及更新每颗子弹的位置。"""
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # 创建Play按钮。
        self.play_buttom = Button(self, "Play")

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_events(self):
        """响应按键和鼠标事件。"""
        # 监视键盘和鼠标事件。
        for event in pygame.event.get():
            # 在这个循环中，我们将编写一系列if 语句来检测并响应特定的事件
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 用鼠标单击Play按钮时做出响应
                # pygame.mouse.get_pos() ，它返回一个元组，其中包含玩家单击时鼠标的x,y坐标
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """响应按键"""
        # 检查按下键（event.key ）是否是右箭头键（pygame.K_RIGHT ）
        if event.key == pygame.K_RIGHT:
            # 向右移动飞船
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # 向左移动飞船
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            # 空格发射
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应松开"""
        # 检查弹起键（event.key ）是否是右箭头键（pygame.K_RIGHT ）
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_play_button(self, mouse_pos):
        """在玩家单击Play按钮时开始新游戏"""
        button_clicked = self.play_buttom.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # 重置游戏统计信息
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            # 清空余下的外星人和子弹。
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群新的外星人并让飞船居中
            self._create_fleet()
            self.ship.center_ship()
            # 隐藏鼠标光标:通过向set_visible() 传递False ，让Pygame在光标位于游戏窗口内时将其隐藏
            pygame.mouse.set_visible(False)

    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹。"""
        self.bullets.update()  # 将为编组bullets 中的每颗子弹调用
        # 删除消失的子弹。
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _update_aliens(self):
        """更新外星人群中所有外星人的位置。"""
        self._check_fleet_edges()
        self.aliens.update()
        # 检测外星人和飞船之间的碰撞。
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            # print("Ship hit!!!")
            self._ship_hit()
        # 检查是否有外星人到达了屏幕底端
        self._check_aliens_bottom()

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)   # 创建一个Bullet 实例
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """创建外星人群。"""
        # 创建一个外星人并计算一行可容纳多少个外星人。
        # 外星人的间距为外星人宽度。
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # 计算屏幕可容纳多少行外星人。
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height)
                             - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        # 创建第一行外星人
        """
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
        """
        # 随机生成外星人
        for num in range(5):
            row_number = randint(0, number_rows)
            alien_number = randint(0, number_aliens_x)
            self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """创建一个外星人并将其放在当前行。"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_bullet_alien_collisions(self):
        """响应子弹和外星人碰撞。"""
        # 删除发生碰撞的子弹和外星人。
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            # 删除现有的子弹并新建一群外星人。
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # 提高等级。
            self.stats.level += 1
            self.sb.prep_level()

    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施。"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                """如果check_edges() 返回True ，就表明相应的外星人位于屏幕边缘，
                需要改变外星人群的方向，因此调用_change_fleet_direction() 并退出循环"""
                self._change_fleet_direction()
                break

    def _check_aliens_bottom(self):
        """检查是否有外星人到达了屏幕底端。"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被撞到一样处理。
                self._ship_hit()
                break

    def _change_fleet_direction(self):
        """将整群外星人下移，并改变它们的方向。"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """响应飞船被外星人撞到。"""
        if self.stats.ships_left > 0:
            # 将ships_left减1。
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            # 清空余下的外星人和子弹。
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群新的外星人，并将飞船放到屏幕底端的中央
            self._create_fleet()
            self.ship.center_ship()
            # 暂停
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕。"""
        # 每次循环时都重绘屏幕。。方法fill() 用于处理surface，只接受一个实参：一种颜色。
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            # 方法bullets.sprites() 返回一个列表，其中包含编组bullets 中的所有精灵
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # 显示得分。
        self.sb.show_score()
        # 如果游戏处于非活动状态，就绘制Play按钮。
        if not self.stats.game_active:
            self.play_buttom.draw_button()
        # 让最近绘制的屏幕可见。它在每次执行while 循环时都绘制一个空屏幕，并擦去旧屏幕
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()
