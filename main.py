import os
import re
import pytesseract
from PIL import Image
# Directory containing the images
directory = './picture/'

# List to store image names
image_names = []

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file ends with '.jpeg' (case-insensitive)
    if filename.lower().endswith('.jpeg'):
        # Add the image name to the list
        image_names.append(filename)
        
for filename in image_names:
    # Open the image file
    image = Image.open(f'./picture/{filename}')
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
    # Perform OCR using PyTesseract
    text = pytesseract.image_to_string(image)
    # text= "+65 9184 8491"
    phone_pattern = r'\+\d{1,9}\s?\d{1,9}[-\s]?\d{1,9}'
    # Print the extracted text
    # print(text)
    phone_numbers = re.findall(phone_pattern, str(text))
    for phone_number in phone_numbers:
        with open('phone_numbers.txt', 'a') as file:
            file.write(phone_number + '\n')