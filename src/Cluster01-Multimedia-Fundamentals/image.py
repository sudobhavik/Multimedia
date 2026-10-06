import cv2
import matplotlib.pyplot as plt
import os

# Try to find sample image in datasets folder
img_path = os.path.join(os.path.dirname(__file__), "..", "datasets", "image.jpg")
if not os.path.exists(img_path):
    img_path = "image.jpg" # Fallback

# Read image
img = cv2.imread(img_path)

# Check whether image was loaded
if img is None:
    print(f"Error: Could not load image from '{img_path}'")
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


# Display/Save images
plt.figure(figsize=(10, 5))
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

# Save the figure
output_path = os.path.join(os.path.dirname(__file__), "grayscale_output.png")
plt.savefig(output_path)
print(f"Saved grayscale output visualization to {output_path}")

try:
    plt.show()
except Exception:
    print("Could not display plot (headless environment), but visualization was saved successfully.")
