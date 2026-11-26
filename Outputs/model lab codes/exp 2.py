
import cv2
import numpy as np

# Read image
img = cv2.imread("input.jpg")

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define green color range
lower = np.array([35, 50, 50])
upper = np.array([85, 255, 255])

# Create binary mask
mask = cv2.inRange(hsv, lower, upper)

# Extract foreground object
result = cv2.bitwise_and(img, img, mask=mask)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Binary Mask", mask)
cv2.imshow("Extracted Foreground", result)

# Save output
cv2.imwrite("segmented_output.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
