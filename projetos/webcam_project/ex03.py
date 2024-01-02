import cv2, pathlib

currentdir = pathlib.Path(__file__).parent

alg_face = cv2.CascadeClassifier((currentdir / "haarcascades" / "haarcascade_frontalface_default.xml").__str__())
alg_eye = cv2.CascadeClassifier((currentdir / "haarcascades" / "haarcascade_eye.xml").__str__())


img = cv2.imread((currentdir / "imagens" / "img2.jpg").__str__())

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

number_of_faces = alg_face.detectMultiScale(img_gray, 1.102, 1, minSize=(10, 10))

for x, y, width, height in number_of_faces:
    img = cv2.rectangle(img, (x, y), (x +width, y+ height), (0, 255, 0), 2) #Armazena imagem com retangulo desenhado

    local_eye = img[y:y + height, x:x + width]
    eye_gray = cv2.cvtColor(local_eye, cv2.COLOR_BGR2GRAY)

    eyes_cords = alg_eye.detectMultiScale(eye_gray)

    for xo, yo, widtho, heighto in eyes_cords:
        cv2.rectangle(local_eye, (xo, yo), (xo + widtho, yo + heighto), (0, 255, 0), 2)

print(number_of_faces)

cv2.imshow("q", img)
cv2.waitKey()