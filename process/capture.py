import win32gui
import win32ui
import win32con
import numpy as np
import cv2

def window_capture(filename):
    # 窗口的编号，0号表示当前活跃窗口
    hwnd = 0

    # 根据窗口句柄获取窗口的设备上下文DC（Device Context）
    hwndDC = win32gui.GetWindowDC(hwnd)

    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)

    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()

    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()

    # 获取监控器信息
    # MoniterDev = win32api.EnumDisplayMonitors(None, None)
    # w = MoniterDev[0][2][2]
    # h = MoniterDev[0][2][3]
    w = 1280
    h = 800

    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, 1280, 800)

    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)

    # 截取从左上角(640,400) 到 (1920,1200)的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (640, 400), win32con.SRCCOPY)

    # 保存bitmap到文件
    saveBitMap.SaveBitmapFile(saveDC, filename)

def window_capture2mat():
    # Window handle (0 for the active window)
    hwnd = 0

    # Get the device context (DC) of the window based on the handle
    hwndDC = win32gui.GetWindowDC(hwnd)

    # Create an MFC DC from the window's DC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)

    # Create a compatible DC for saving
    saveDC = mfcDC.CreateCompatibleDC()

    # Create a bitmap to save the image
    saveBitMap = win32ui.CreateBitmap()

    # Monitor resolution (adjust as needed)
    w = 1280
    h = 800

    # Allocate space for the bitmap
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    # Select the bitmap into the saveDC
    saveDC.SelectObject(saveBitMap)

    # Capture the image from (640, 400) to (1920, 1200)
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (640, 400), win32con.SRCCOPY)

    # Get the bitmap bits
    signedIntsArray = saveBitMap.GetBitmapBits(True)
    img = np.frombuffer(signedIntsArray, dtype='uint8')
    img.shape = (h, w, 4)

    # Free resources
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    # Drop the alpha channel, or cv2.cvtColor will throw an error
    # because of the extra channel
    img = img[..., :3]

    # Convert to BGR format for OpenCV
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    return img

def window_capture2pic(filename):
    img = window_capture2mat()
    cv2.imwrite(filename, img)

if __name__ == '__main__':
    import time
    import subprocess

    # 1  100 -> 120
    # 2  200 -> 245
    # 3  300 -> 385

    # 1.25 100 -> 138 200 -> 300

    # 100 - 184
    # 200 - 370
    time.sleep(5)
    window_capture2pic('test.jpg')
    # D:\My_C\ai\cheat\test.exe
    subprocess.run('D:\\My_C\\ai\\cheat\\test.exe')
    time.sleep(5)
    window_capture2pic('test2.jpg')
    




