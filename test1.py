from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pytesseract
import enum

class OS(enum.Enum):
    Mac = 0
    Windows = 1

class Language(enum.Enum):
    ENG = 'eng'
    RUS = 'rus'
    ITA = 'ita'
    DEU = 'deu'

class ImageReader:
    def __init__(self, os: OS):
        if os == OS.Mac:
            print('Running on: MAC\n')
        if os == OS.Windows:
            windows_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            pytesseract.pytesseract.tesseract_cmd = windows_path
            print('Running on: Windows\n')

# Load image
img = np.array(Image.open('test_imgs\meme7.jpg'))

# Display plain image
plt.figure(figsize=(10, 10))
plt.title('PLAIN IMAGE')
plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()

# Perform OCR on plain image with psm and oem parameters
text = pytesseract.image_to_string(img, config='--psm 12 --oem 3')  # Adjust psm and oem values as needed
print(text.replace('\n', ' '))

# Apply bilateral filter
img = cv2.bilateralFilter(img, 5, 55, 60)

# Display image after bilateral filter
plt.figure(figsize=(10, 10))
plt.title('BILATERAL FILTER')
plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()

# Convert to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display grayscale image
plt.figure(figsize=(10, 10))
plt.title('GRAYSCALE IMAGE')
plt.imshow(img, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

# Binarize image
_, img = cv2.threshold(img, 240, 255, 1)

# Display binary image
plt.figure(figsize=(10, 10))
plt.title('IMMAGINE BINARIA')
plt.imshow(img, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

# Define the correct function name
def preprocess_finale(img):
    img = cv2.bilateralFilter(img, 5, 55, 60)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 240, 255, 1)
    return img

# Load image again for preprocessing
img = np.array(Image.open('test_imgs\meme8.jpg'))

# Preprocess image using the correct function name
img = preprocess_finale(img)

# Perform OCR on preprocessed image with psm and oem parameters
text = pytesseract.image_to_string(img, lang='eng', config='--psm 12 --oem 3')  # Adjust psm and oem values as needed
print(text.replace('\n', ' '))
