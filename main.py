from pytube import YouTube
from time import sleep
import webbrowser
from skimage.metrics import structural_similarity as ssim
import cv2

def main():
    video_url = "https://www.youtube.com/watch?v=H7N2nvBdZ4g&autoplay=1"
    yt = YouTube(video_url)
    webbrowser.open(video_url)
    print("Playing YouTube video:")

image1 = cv2.imread("./images/screenshot_2024-12-08_18-06-02.png")
image2 = cv2.imread("./images/screenshot_2024-12-08_18-06-04.png")

def compare_images(image_1, image_2):
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    similarity_index, _ = ssim(gray1, gray2, full=True)
    return similarity_index

if __name__=="__main__":
    main()
    
    # Holds latest taken screenshot
    latest_screenshot = None
    
    # Image settings
    x, y = 252, 701
    width, height = 1400, 225
    
    while True:
        if not latest_screenshot:
            pass
            # Take screen shot for latest
        else:
            pass
            # Take screen shot and compare to latest
            # If SSIM < 0.9, save latest to file and update latest_screenshot
        sleep(1)