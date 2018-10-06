"""
创建Pygame窗口以及相应用户输入
设置背景颜色
"""

import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('外星人入侵')

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于子弹的编组
    bullets = Group()

    # 游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)


if __name__ == '__main__':
    run_game()
