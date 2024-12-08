import pyautogui
import time
import keyboard
import datetime

def take_screenshot(x, y, width, height):
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_filename = f"./images/screenshot_{timestamp}.png"
    
    screenshot.save(screenshot_filename)
    print(f"Screenshot taken and saved as {screenshot_filename}")

def main():
    print("Press 's' to take a screenshot.")
    print("Press 'c' to exit.")
    
    x, y = 252, 701
    width, height = 1400, 225
    
    while True:
        if keyboard.is_pressed('s'):
            take_screenshot(x, y, width, height)
            time.sleep(1)
        if keyboard.is_pressed('c'):
            print("Exiting...")
            break

if __name__ == "__main__":
    main()