
import cv2
import numpy as np

# Read image
img = cv2.imread("input.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
ret, binary = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY
)

# Create structuring element
kernel = np.ones((5, 5), np.uint8)

# Morphological opening
opening = cv2.morphologyEx(
    binary, cv2.MORPH_OPEN, kernel
)

# Morphological closing
closing = cv2.morphologyEx(
    binary, cv2.MORPH_CLOSE, kernel
)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Binary Image", binary)
cv2.imshow("Morphological Opening", opening)
cv2.imshow("Morphological Closing", closing)

# Save outputs
cv2.imwrite("opening_output.jpg", opening)
cv2.imwrite("closing_output.jpg", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
