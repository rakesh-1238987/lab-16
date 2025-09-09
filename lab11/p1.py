import cv2
import numpy as np


img = cv2.imread("C:/Users/ADMIN/Downloads/download.jpeg")


if img is None:
    print("Error: Image not found. Check the file path!")
    exit()
height, width, channels = img.shape
print("Image Dimensions: ", (height, width))
print("Image Shape: ", img.shape)
min_blue = np.min(img[:, :, 0])
print("Minimum Pixel Value at Blue Channel:", min_blue)

padded_img = cv2.copyMakeBorder(
    img,
    50, 50, 100, 100,             
    cv2.BORDER_CONSTANT,
    value=(0, 0, 0)                 
)
cv2.imshow("Original Image", img)
cv2.imshow("Padded Image", padded_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("C:/Users/ADMIN/Downloads/padded_image.jpeg", padded_img)
print("Padded image saved as padded_image.jpeg")
