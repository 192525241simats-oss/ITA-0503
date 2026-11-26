
import cv2
import numpy as np

# Read image
img = cv2.imread("input.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel X - Vertical edges
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_x = cv2.convertScaleAbs(sobel_x)

# Sobel Y - Horizontal edges
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Combined gradient magnitude
magnitude = cv2.magnitude(
    cv2.Sobel(gray, cv2.CV_32F, 1, 0),
    cv2.Sobel(gray, cv2.CV_32F, 0, 1)
)
magnitude = cv2.convertScaleAbs(magnitude)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Vertical Edges", sobel_x)
cv2.imshow("Horizontal Edges", sobel_y)
cv2.imshow("Combined Edges", magnitude)

cv2.waitKey(0)
cv2.destroyAllWindows()
