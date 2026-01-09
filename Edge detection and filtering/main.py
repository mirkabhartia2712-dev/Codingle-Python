import cv2

import numpy as np

import matplotlib.pyplot as plt

def display_image(title, image):

    """Utility function to display an image."""

    plt.figure(figsize=(8,8))

    if len(image.shape) == 2:

        plt.imshow(image, cmap='gray')
    
    else:

        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.title(title)

    plt.axis('off')

    plt.show()

def interactive_edge_detective(image_path):

    """Interactive activity for edge detection and filtering."""

    image = cv2.imread(image_path)

    if image is None:

        print ("Error: Image not found!")

        return
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("Original Grayscale Image", gray_image)

    print("Select an option:")

    print("1. Sobel Edge Detection")

    print ("2. Canny Edge Detection")

    print("3. Laplacian Edge Detection")

    print("4. Gaussian Smoothing")

    print("5. Median Filtering")

    print("6. Exit")

    while True:

        choice = input("Enter your choice (1-6): ")

        if choice == "1":

            sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)

            sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0,1, ksize=3)

            combined_sobel= 
