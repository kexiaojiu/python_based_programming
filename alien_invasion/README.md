[toc]
---
# 1 项目规划
在游戏《外星人入侵》中，玩家控制着一艘最初出现在屏幕底部中央的飞船。玩家可以使用箭头键左右移动飞船，还可以使用空格键进行射击。 游戏开始时，一群外星人出现在天空，他们在屏幕中向下移动。玩家的任务是射杀这些外星人。玩家将所有外星人都消灭干净后，将出现一群新的外星人，他们的移动速度更快。只要有外星人撞到了玩家的飞船或者到底屏幕底部，玩家就损失一条飞船。玩家损失三条飞船后，游戏结束。
第一阶段，我们将创建一艘可左右移动的飞船，这艘飞船在用户按空格键时能够开火。
第二阶段，我们将开发外星人模块。
第三阶段，我们将提高游戏的可玩性。

# 2 项目准备
电脑系统：ubuntun 16.04.2
开发工具：geany
开发语言：python(python 3.5)
安装软件：
--- pip: https://pip.pypa.io/en/stable/installing/
--- Pygame：https://bitbucket.org/pygame/pygame/downloads/
```
$ sudo apt install python3-pip
$ pip3 install pygame
```

# 3 文件说明
* alien_invasion.py 运行该文件就可以玩《外星人入侵》，其他文件都会被直接或者间接导入其中。创建一些列游戏所需的对象，如存储在ai_setting中的设置，存储在screen中的主显示surface、一个飞船、子弹实例。
* ship.py 飞船类，包含方法__init__()、管理飞船位置的方法update()以及在屏幕上绘制飞船的方法blitme()。
* images 存放所有图像
* settings.py 存放所有参数，只有方法__init__()，初始化控制游戏外观和飞船速度的属性
* game_functions.py 事件管理函数。函数check_event()检测相关事件，如按键和松开；update_screen()函数，每次执行主循环时候都会重绘屏幕；fire_bullet()发射子弹；update_bullets()更新子弹，删除消失在屏幕的子弹
* bullet.py 子弹类，包含方法__init__()、update()子弹向上移动、draw_bullet()在屏幕绘制子弹
