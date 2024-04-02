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
        if listener.tag_shift:
            img = process.capture.window_capture2mat()
            best_pos = yolo_pre.bestshot(img)
            print(f'best_pos: {best_pos}')

            if best_pos is not None:
                print('开始移动鼠标')
                mouse_move.move_smooth(best_pos)
                print('鼠标移动完成')
            time.sleep(0.1)

if __name__ == '__main__':
    main()
    