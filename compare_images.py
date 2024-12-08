import cv2

# Load images
# image1 = cv2.imread("./images/image_to_compare.PNG")
image1 = cv2.imread("./images/1.PNG")
image2 = cv2.imread("./images/4.PNG")

# 244 225 214
# 243 225 214
# 243 226 212
hist_img1 = cv2.calcHist([image1], [0, 1 ,2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
hist_img1[255, 255, 255] = 0 # Ignores white pixels, maybe bad if tabs has many white pixels, look into later
hist_img1[244, 225, 241] = 0
hist_img1[243, 225, 241] = 0
hist_img1[243, 226, 212] = 0
cv2.normalize(hist_img1, hist_img1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

hist_img2 = cv2.calcHist([image2], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
hist_img2[255, 255, 255] = 0
hist_img2[244, 225, 241] = 0
hist_img2[243, 225, 241] = 0
hist_img2[243, 226, 212] = 0
cv2.normalize(hist_img2, hist_img2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

metric_val = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_CORREL)
print(f"Similarity Score: ", metric_val)