from pynput import keyboard
from pynput import mouse

class Listener:
    def __init__(self):
        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.tag_right = False
        self.tag_x1 = False
        self.tag_shift = False
    
    def on_click(self, x, y, button, pressed):
         if pressed:
            if button == mouse.Button.right:
                self.tag_right = not self.tag_right
                print(f'tag_right: {self.tag_right}')
            elif button == mouse.Button.x1:
                self.tag_x1 = not self.tag_x1
                print(f'tag_x1: {self.tag_x1}')

    def on_press(self, key):
            if key == keyboard.Key.shift_r:
                self.tag_shift = not self.tag_shift
                print(f'tag_shift: {self.tag_shift}')

    def on_release(self, key):
        if key == keyboard.Key.esc:
            # 按下ESC键退出监听
            self.mouse_listener.stop()
            self.keyboard_listener.stop()
            return False
        
    def start(self):
        self.mouse_listener.start()
        self.keyboard_listener.start()
        self.mouse_listener.join()
        self.keyboard_listener.join()

if __name__ == '__main__':

    listener = Listener()
    listener.start()
