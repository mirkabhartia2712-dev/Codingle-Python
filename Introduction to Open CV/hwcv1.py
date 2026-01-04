import cv2


image = cv2.imread('example.jpg')

resized_image = cv2.resize((200, 200))
resized_image = cv2.resize((400, 400))
resized_image = cv2.resize((600, 600))

cv2.imshow('Processed Image', resized_image)


key = cv2.waitKey(0)


if key == ord('s'):

    cv2.imwrite('resized_image.jpg', resized_image)
    print ("image saved as resized_image.jpg")
else:
    print("Image not saved")


cv2.destroyAllWindows()


print(f"Processed Image Dimensions: {resized_image.shape}")