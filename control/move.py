import numpy as np
import ctypes
import os

'''
extern "C" {
    DLL_EXPORT void move_relpix(int x, int y);
    DLL_EXPORT void move_gamepix(int x, int y);
    DLL_EXPORT void move_smooth(int x, int y, int n);
}
'''
class MouseMove:
    def __init__(self):
        dllname = 'move.dll'
        if not os.path.exists(dllname):
            raise FileNotFoundError(f'{dllname} not found')
        dllpath = os.path.abspath(dllname)
        self.move_dll = ctypes.windll.LoadLibrary(dllpath)
        self.move_dll.move_relpix.argtypes = [ctypes.c_int, ctypes.c_int]
        self.move_dll.move_relpix.restype = None
        self.move_dll.move_gamepix.argtypes = [ctypes.c_int, ctypes.c_int]
        self.move_dll.move_gamepix.restype = None
        self.move_dll.move_smooth.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
        self.move_dll.move_smooth.restype = None

    def rel_pos(self, best_pos):
        center_pos = np.array([640, 400])
        return (best_pos - center_pos).astype(int)
    
    def move_relpix(self, best_pos):
        if best_pos is None:
            return
        best_pos = self.rel_pos(best_pos)
        self.move_dll.move_relpix(ctypes.c_int(best_pos[0]), ctypes.c_int(best_pos[1]))

    def move_gamepix(self, best_pos):
        if best_pos is None:
            return
        best_pos = self.rel_pos(best_pos)
        self.move_dll.move_gamepix(ctypes.c_int(best_pos[0]), ctypes.c_int(best_pos[1]))

    def move_smooth(self, best_pos, n = 50):
        if best_pos is None:
            return
        best_pos = self.rel_pos(best_pos)
        self.move_dll.move_smooth(ctypes.c_int(best_pos[0]), ctypes.c_int(best_pos[1]), ctypes.c_int(n))

# def move(best_pos):
#     center_pos = np.array([640, 400])
#     best_pos = np.array(best_pos)
#     move_rela = best_pos - center_pos
#     print(f'move_rela: {move_rela}')
#     # 获取当前鼠标位置
#     x, y = pydirectinput.position()
#     # 移动到最佳位置
#     now_pos = np.array([x, y])
#     print(f'now_pos: {now_pos}')
#     delta = (move_rela * alpha).astype(int)
#     time_start = time.time()
#     dest_pos = now_pos + move_rela
#     print(f'dest_pos: {dest_pos}')

#     while np.linalg.norm(dest_pos - now_pos) > loss:
#         pydirectinput.moveRel(delta[0], delta[1], relative=True)
#         x, y = pydirectinput.position()
#         now_pos = np.array([x, y])
#         delta = ((dest_pos - now_pos) * alpha).astype(int)
#         print(f'dest_pos: {dest_pos}')
#         print(f'now_pos: {now_pos}')
#         time.sleep(0.1)
    

if __name__ == '__main__':
    import time
    mouse_move = MouseMove()
    # now = time.time()
    # mouse_move.move_relpix([800, 800])
    # print('Time elapsed:', time.time() - now)
    # now = time.time()
    # mouse_move.move_gamepix([800, 800])
    # print('Time elapsed:', time.time() - now)
    time.sleep(5)
    now = time.time()
    mouse_move.move_smooth(np.array([800.1, 800.2]))
    print('Time elapsed:', time.time() - now)
    
    
    