import cv2

image = cv2.imread("dog.jpg")
(h, w, c) = image.shape[:3]

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

print(f'channels: {c}')

image_gray = cv2.imread("dog.jpg", cv2.IMREAD_GRAYSCALE)
(h, w, c) = image.shape[:3]


print(f'channels: {c}')

cv2.imwrite("dog_gray.jpg", image_gray)

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.namedWindow("image_gray", cv2.WINDOW_NORMAL)

cv2.imshow("image", image)
cv2.imshow("image_gray", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()