from pynput import mouse

class CoordinateLogger:
    def __init__(self):
        self.start_x = None  # ドラッグ開始位置のX座標
        self.start_y = None  # ドラッグ開始位置のY座標
        self.end_x = None    # ドラッグ終了位置のX座標
        self.end_y = None    # ドラッグ終了位置のY座標

    def on_click(self, x, y, button, pressed):
        if pressed:
            if self.start_x is None and self.start_y is None:
                # マウスボタンが押された時の座標を記録
                self.start_x, self.start_y = x, y
                print(f"Start position: ({self.start_x}, {self.start_y})")
            else:
                # マウスボタンが押されたままドラッグしている時の座標を更新
                self.end_x, self.end_y = x, y
                #print(f"Current position: ({self.end_x}, {self.end_y})")

        if not pressed:
            # マウスボタンが離された時の座標を記録
            self.end_x, self.end_y = x, y
            print(f"End position: ({self.end_x}, {self.end_y})")
            print(f"Selected area: ({self.start_x}, {self.start_y}) to ({self.end_x}, {self.end_y})")

            self.coordinates = {
                'start': (self.start_x, self.start_y),
                'end': (self.end_x - self.start_x, self.end_y - self.start_y)
            }

            return False
        
    def on_move(self, x, y):
        if self.start_x is not None and self.start_y is not None:
            # ドラッグ中の座標を更新
            self.end_x, self.end_y = x, y
            #print(f"Current position: ({self.end_x}, {self.end_y})")
            
    def start(self):
        global listener
        # マウスイベントリスナーを開始
        with mouse.Listener(on_click=self.on_click, on_move=self.on_move) as listener:
            try :
                listener.start()
                listener.join()
                print("リスナーを再生成しました")
            except:
                listener.join()

    def __del__(self):
        listener.stop()
        print("マウスの監視を停止しました。")