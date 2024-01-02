import cv2, pathlib, os
currentdir = pathlib.Path(__file__).parent

alg = cv2.CascadeClassifier((currentdir / "haarcascades" / "haarcascade_frontalface_default.xml").__str__())

img = cv2.imread((currentdir / "imagens" / "img3.jpg").__str__())

imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = alg.detectMultiScale(imggray)

print(faces)

for x, y, width, height in faces:
    cv2.rectangle(img, (x, y), (x + width, y + height), (255, 0, 0), 2)
    

cv2.imshow("faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()