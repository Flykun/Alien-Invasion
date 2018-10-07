"""创建设置类"""


class Settings():
    """存储<外星人入侵>的所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 11  # 最大存在子弹数量
        self.alien_speed_factor = 1  # 外星人速度
        self.fleet_drop_speed = 10  # 外星人下移速度
        self.fleet_direction = 1  # 右一

        # 飞船设置
        self.ship_speed_factor = 1.5
