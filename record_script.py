import os
import sys
import cv2
import numpy as np
import subprocess
import time
import mss
import win32con
import win32gui


argv = sys.argv
# ========================== 參數設定區 ==========================

PKG_ROOT = argv[1]
VIDEO_TAG = argv[2] if len(argv) == 3 else ""
# PKG_ROOT = "E:\share2\M11215119\PyAutoDriveRL-Env"
os.chdir(PKG_ROOT)

student_id = PKG_ROOT.split(os.sep)[-2]
print(student_id)

# 基本參數
END_TIME = 65  # 錄製結束時間，單位：秒
VIDEO_PATH = fr"C:\Users\miisl\PyAutoDriveRL-Env\results/{student_id}_{VIDEO_TAG}.mp4"  # 錄製影片的存檔路徑
VIDEO_WIDTH = 720  # 錄製影片的寬度
VIDEO_HEIGHT = 640  # 錄製影片的高度
FPS = 30  # 每秒幀數（Frames Per Second）

# 目標窗口設定
WINDOW_TITLE = 'Car'  # 目標窗口名稱（需與目標窗口標題一致）

# 子程序腳本路徑
RESET_SCRIPT_PATH = r"C:\Users\miisl\miniconda3\envs\autodrive_rl\python.exe"
RESET_SCRIPT_NAME = r"C:\Users\miisl\PyAutoDriveRL-Env\reset_script.py"
INFERENCE_SCRIPT_NAME = "inference_template.py"

# ============================================================


# ========================== 功能函數 ==========================
def countdown_display(frame, remaining_time):
    """
    在畫面中央顯示倒數計時。
    :param frame: 目前的影像幀
    :param remaining_time: 倒數的剩餘時間
    :return: 添加倒數計時後的影像幀
    """
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (255, 255, 255)  # 白色
    thickness = 30
    font_scale = 20

    # 將剩餘時間轉換為文字
    text = str(remaining_time)

    # 計算文字尺寸，確保居中顯示
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    text_width, text_height = text_size
    text_x = (frame.shape[1] - text_width) // 2
    text_y = (frame.shape[0] + text_height) // 2 + 50

    # 將倒數文字寫入畫面
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, color, thickness, cv2.LINE_AA)
    return frame


def text_log_display(frame, text):
    """
    在畫面頂部顯示日誌文字。
    :param frame: 目前的影像幀
    :param text: 要顯示的文字內容
    :return: 添加日誌文字後的影像幀
    """
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (255, 255, 255)  # 白色
    thickness = 2
    font_scale = 1

    # 計算文字尺寸
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    text_width, text_height = text_size
    text_x = (frame.shape[1] - text_width) // 2
    text_y = 75  # 固定顯示於畫面頂部

    # 將文字寫入畫面
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, color, thickness, cv2.LINE_AA)
    return frame


def ID_display(frame):
    """
    在畫面頂部顯示日誌文字。
    :param frame: 目前的影像幀
    :return: 添加文字後的影像幀
    """
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (255, 255, 255)  # 白色
    thickness = 3
    font_scale = 1.5

    # 計算文字尺寸
    text_size = cv2.getTextSize(student_id, font, font_scale, thickness)[0]
    text_width, text_height = text_size
    text_x = (frame.shape[1] - text_width) // 2
    text_y = 130  # 固定顯示於畫面頂部

    # 將文字寫入畫面
    cv2.putText(frame, student_id, (text_x, text_y), font, font_scale, color, thickness, cv2.LINE_AA)
    return frame


def get_all_hwnd(hwnd, mouse):
    """
    獲取所有窗口句柄，存入全域變數 `hwnd_map` 中。
    """
    if (win32gui.IsWindow(hwnd) and
            win32gui.IsWindowEnabled(hwnd) and
            win32gui.IsWindowVisible(hwnd)):
        hwnd_map.update({hwnd: win32gui.GetWindowText(hwnd)})


def put_video_foreground():
    """
    將目標窗口放置到前台。
    """
    for h, t in hwnd_map.items():
        if t and t == WINDOW_TITLE:
            # 將窗口放到最前面
            win32gui.SetForegroundWindow(h)
            # 若窗口被最小化，恢復顯示
            win32gui.ShowWindow(h, win32con.SW_RESTORE)


# ========================== 主程序 ==========================
def record_video():
    """
    主錄製函數，執行整個錄製流程。
    """
    os.makedirs(os.path.dirname(VIDEO_PATH), exist_ok=True)

    # 設定影片的錄製編碼
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(VIDEO_PATH, fourcc, FPS, (VIDEO_WIDTH, VIDEO_HEIGHT))

    hwnd = win32gui.FindWindow(None, WINDOW_TITLE)  # 根據窗口名稱查找句柄
    if not hwnd:
        print(f"Error: 找不到名為 '{WINDOW_TITLE}' 的窗口")
        return

    left, top, right, bottom = win32gui.GetWindowRect(hwnd)  # 獲取窗口邊界
    left += VIDEO_WIDTH // 3 - 10
    right += VIDEO_WIDTH // 2
    top += 10
    bottom += VIDEO_HEIGHT // 3 - 75
    put_video_foreground()  # 將窗口放置到前台

    # 啟動 ResetScript.py
    proc = subprocess.Popen([RESET_SCRIPT_PATH, RESET_SCRIPT_NAME])
    proc.wait()
    proc = subprocess.Popen([RESET_SCRIPT_PATH, RESET_SCRIPT_NAME])
    proc.wait()

    # 使用 mss 捕獲窗口
    with mss.mss() as sct:
        monitor = {"top": top, "left": left + 10, "width": right - left - 20, "height": bottom - top}

        try:
            # 倒數3秒
            for remaining_time in range(3, 0, -1):
                for _ in range(FPS):
                    img = np.array(sct.grab(monitor))
                    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
                    img = countdown_display(img, remaining_time)
                    img = text_log_display(img, "Initializing...")
                    img = ID_display(img)
                    out.write(cv2.resize(img, (VIDEO_WIDTH, VIDEO_HEIGHT)))
                    cv2.imshow("Recording", img)
                    cv2.waitKey(1)

            # 啟動模型推論腳本
            print("Starting inference...")
            proc = subprocess.Popen([RESET_SCRIPT_PATH, INFERENCE_SCRIPT_NAME])

            frame_time = 1 / FPS
            start_time = time.time()
            tmp_time = time.time()
            while time.time() - start_time < END_TIME:
                remaining_time = END_TIME - (time.time() - start_time)

                img = np.array(sct.grab(monitor))
                img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
                img = text_log_display(img, "Running inference_template.py..., {:.1f} s".format(remaining_time))
                img = ID_display(img)

                if time.time() - tmp_time >= frame_time:
                    out.write(cv2.resize(img, (VIDEO_WIDTH, VIDEO_HEIGHT)))
                    tmp_time += frame_time  # 增加时间间隔，而不是重置为当前时间

                # 显示窗口
                cv2.imshow("Recording", img)
                print(f"\r Remaining time: {remaining_time:.1f} seconds", end="")
                if cv2.waitKey(1) & 0xFF == 27:  # ESC 键退出
                    break
            print()

            img = np.array(sct.grab(monitor))
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            img = text_log_display(img, "Recording finished, showing final frame...")
            img = ID_display(img)

            # 停止推論腳本
            proc.terminate()
            proc.wait()

            proc = subprocess.Popen([RESET_SCRIPT_PATH, RESET_SCRIPT_NAME])

            # 停留最後一幀3秒
            print("Recording finished, showing final frame...")
            for _ in range(3 * FPS):
                out.write(cv2.resize(img, (VIDEO_WIDTH, VIDEO_HEIGHT)))
                cv2.imshow("Recording", img)
                if cv2.waitKey(1000 // FPS) & 0xFF == 27:
                    break

            proc = subprocess.Popen([RESET_SCRIPT_PATH, RESET_SCRIPT_NAME])

            # 淡出處理
            for i in range(30):
                alpha = 1 - i / 30.0
                faded_frame = cv2.addWeighted(img, alpha, np.zeros_like(img), 0, 0)
                out.write(cv2.resize(faded_frame, (VIDEO_WIDTH, VIDEO_HEIGHT)))
                cv2.imshow("Recording", faded_frame)
                if cv2.waitKey(1000 // FPS) & 0xFF == 27:
                    break

            proc = subprocess.Popen([RESET_SCRIPT_PATH, RESET_SCRIPT_NAME])
            proc.wait()

        finally:
            # 釋放資源
            print("Releasing resources...")
            out.release()
            cv2.destroyAllWindows()


# ========================== 主程式入口 ==========================
if __name__ == "__main__":
    hwnd_map = {}
    win32gui.EnumWindows(get_all_hwnd, 0)  # 獲取所有窗口句柄
    record_video()
