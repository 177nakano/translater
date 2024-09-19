from pynput import mouse
from pynput import keyboard
import sys

class Test_CoordinateLogger:
    def __init__(self):
        self.x = None
        self.y = None

    def on_move(self, x, y):
        if self.x is None and self.y is None:
            # マウスボタンが押された時の座標を記録
            self.x, self.y = x, y
            print(f"Start position: ({self.x}, {self.y})")
        else:
            # マウスボタンが押されたままドラッグしている時の座標を更新
            self.x, self.y = x, y
            print(f"Current position: ({self.x}, {self.y})")

    def on_press(self,key):
        if key == keyboard.Key.esc:
            self.mouse_listener.stop()
            self.keyboard_listener.stop()
            return False
            #return False
        
    def start(self):
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press)
        self.mouse_listener = mouse.Listener(on_move=self.on_move)

        self.keyboard_listener.start()
        self.mouse_listener.start()

        # 両方のリスナーが停止するまで待機
        self.keyboard_listener.join()
        self.mouse_listener.join()

#monitor = Test_Keyboard_Monitoring()
#monitor.start()
logger = Test_CoordinateLogger()
logger.start()