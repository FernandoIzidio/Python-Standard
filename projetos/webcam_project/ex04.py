import cv2, pathlib

currentdir = pathlib.Path(__file__).parent

alg_face = cv2.CascadeClassifier((currentdir / "haarcascades" / "haarcascade_frontalface_default.xml").__str__())
alg_eye = cv2.CascadeClassifier((currentdir / "haarcascades" / "haarcascade_eye.xml").__str__())

img = cv2.imread((currentdir / "imagens" / "ROSTOS" / "rosto3.jpg").__str__())

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

data_faces = alg_face.detectMultiScale(img_gray)

for x, y, width, height in data_faces:
    img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)

    face_eye = img[y:y + height, x:x + width]

    eye_gray = cv2.cvtColor(face_eye, cv2.COLOR_BGR2GRAY)

    data_eye = alg_eye.detectMultiScale(face_eye)

    for xo, yo, widtho, heighto in data_eye:
        cv2.rectangle(face_eye, (xo, yo), (xo + widtho, yo + heighto), (255, 0, 0), 2)


cv2.imshow("Faces e olhos", img)
cv2.waitKey(0)