import cv2, pathlib
currentdir = pathlib.Path(__file__).parent

alg = cv2.CascadeClassifier((currentdir /  "haarcascades" /  "haarcascade_frontalface_default.xml").__str__())

img = cv2.imread((currentdir / "imagens" / "img4.jpg").__str__())

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

number_of_faces = alg.detectMultiScale(img_gray, 1.30, 4, minSize=(10, 10))

for x, y, width, height in number_of_faces:
    cv2.rectangle(img, (x, y), (x + width, y+ height), (0, 255, 0), 2)

print(number_of_faces)


cv2.imshow("faceswork", img)
cv2.waitKey(0)

