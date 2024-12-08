from skimage.metrics import structural_similarity as ssim
import cv2

image1 = cv2.imread("./images/screenshot_2024-12-08_18-06-02.png")
image2 = cv2.imread("./images/screenshot_2024-12-08_18-06-04.png")

def compare_images(image_1, image_2):
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    similarity_index, _ = ssim(gray1, gray2, full=True)
    return similarity_index

print(f"SSIM similarity score: {compare_images(image1, image2)}")