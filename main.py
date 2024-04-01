import control.listener
import control.move
import process.capture
import detect.yolo_pre
import time
import threading

def main():
    # 第一个线程：监听鼠标和键盘
    listener = control.listener.Listener()
    listener_thread = threading.Thread(target=listener.start)
    listener_thread.start()

    yolo_pre = detect.yolo_pre.YOLOPre()
    print(yolo_pre.prehot('dataset/test/images'))
    print('预热完成')

    mouse_move = control.move.MouseMove()

    while True:
        if not listener.tag_shift:
            listener.tag_x1 = False
        if listener.tag_x1 and listener.tag_shift:
            img = process.capture.window_capture2mat()
            best_pos = yolo_pre.bestshot(img)
            if best_pos is not None:
                mouse_move.move_smooth(best_pos)
            time.sleep(0.1)

if __name__ == '__main__':
    main()