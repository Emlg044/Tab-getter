from pytube import YouTube
from time import sleep
import webbrowser
from skimage.metrics import structural_similarity as ssim
import cv2
import pyautogui
import datetime
import numpy as np

def main():
    # Sultans of swing
    # video_url = "https://www.youtube.com/watch?v=H7N2nvBdZ4g&autoplay=1"
    # Bohemian rhapsody
    video_url = "https://www.youtube.com/watch?v=n1WomoCiYqg&autoplay=1"
    yt = YouTube(video_url)
    webbrowser.open(video_url)
    print("Playing YouTube video:")

# image1 = cv2.imread("./images/screenshot_2024-12-08_18-06-02.png")
# image2 = cv2.imread("./images/screenshot_2024-12-08_18-06-04.png")

def compare_images(image_1, image_2):
    gray1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2GRAY)

    similarity_index, _ = ssim(gray1, gray2, full=True)
    return similarity_index

def take_screenshot(x, y, width, height):
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    
    screenshot_cv = np.array(screenshot)
    screenshot_cv = cv2.cvtColor(screenshot_cv, cv2.COLOR_RGB2BGR)
    
    return screenshot_cv

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_filename = f"./images/screenshot_{timestamp}.png"
    
    screenshot.save(screenshot_filename)
    print(f"Screenshot taken and saved as {screenshot_filename}")

def write_img_to_file(image):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_filename = f"./tabs/screenshot_{timestamp}.png"
    cv2.imwrite(screenshot_filename, image)

if __name__=="__main__":
    main()
    
    # Holds latest taken screenshot
    latest_screenshot = None
    first_has_been_set = False
    
    # Image settings
    x, y = 252, 701
    width, height = 1400, 225
    
    while True:
        sleep(2.5)
        if not first_has_been_set:
            # Take screen shot for latest
            latest_screenshot = take_screenshot(x, y, width, height)
            first_has_been_set = True
        else:
            # Take screen shot and compare to latest
            # If SSIM < 0.9, save latest to file and update latest_screenshot
            new_screenshot = take_screenshot(x, y, width, height)
            similarity_index = compare_images(latest_screenshot, new_screenshot)
            if similarity_index < 0.9:
                write_img_to_file(latest_screenshot)
            latest_screenshot = new_screenshot