# Image to Pencil Sketch Task using cv2 library.
# In this Task I have used Image of Horse to perform the Task.
import cv2

# Image path 
img_loc = "C:/Users/AHanan/Desktop/ImagetoPencil/horse.jpg"

img = cv2.imread(img_loc)
# Gray Image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blurred Image
blurred_img = cv2.GaussianBlur(gray_img, (21,21), 0)
# Pencil to sketch
img_pencil_sketch = cv2.divide(gray_img, blurred_img, scale=256.0)

cv2.imshow("Original Image", img)
cv2.imshow("Pencil to Sketch Image", img_pencil_sketch)
cv2.waitKey(0)
# Saving Image 
cv2.imwrite("ImageToPencilSketch.jpg", img_pencil_sketch)
