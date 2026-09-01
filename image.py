import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("sample.jpg")

# Check whether image was loaded
if img is None:
    print("Error: Could not load image")
    exit()

# BGR order, not RGB
print("shape :", img.shape)

# Example:
# (height, width, 3)

print("dtype :", img.dtype)

# uint8 → values 0..255

print("min/max:", img.min(), img.max())


# Convert BGR image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("gray shape:", gray.shape)

# Example:
# (height, width)
# Channel is gone


# Display images
plt.subplot(1, 2, 1)

# Convert BGR → RGB before displaying with Matplotlib
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("Original")


plt.subplot(1, 2, 2)

# Display grayscale image
plt.imshow(gray, cmap="gray")
plt.axis("off")
plt.title("Grayscale")


plt.show()
