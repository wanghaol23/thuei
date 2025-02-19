import time
import Board

print('''
**********************************************************
********功能:幻尔科技树莓派扩展板，蜂鸣器控制例程*********
**********************************************************
----------------------------------------------------------
Official website:https://www.hiwonder.com
Online mall:https://hiwonder.tmall.com
----------------------------------------------------------
Tips:
 * 按下Ctrl+C可关闭此次程序运行，若失败请多次尝试！
----------------------------------------------------------
''')

Board.setBuzzer(0) # 关闭

Board.setBuzzer(1) # 打开
time.sleep(0.1) # 延时
Board.setBuzzer(0) #关闭

time.sleep(1) # 延时

Board.setBuzzer(1)
time.sleep(0.5)
Board.setBuzzer(0)