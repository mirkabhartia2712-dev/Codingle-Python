import cv2


image = cv2.imread('example.jpg')


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


resized_image = cv2.resize(gray_image, (800, 500))


cv2.imshow('Processed Image', resized_image)


key = cv2.waitKey(0)


if key == ord('s'):

    cv2.imwrite('grayscale_resized_image.jpg', resized_image)
    print ("image saved as grayscale_resized_image.jpg")
else:
    print("Image not saved")


cv2.destroyAllWindows()


print(f"Processed Image Dimensions: {resized_image.shape}")

cv2.getRotationMatrix2D()
cv2.warpAffine()

np.ones()
cv2.add()


output_images
cv2.imwrite()