import cv2, math, pathlib                  
import mediapipe as mp          

VIDEO_PATH = (pathlib.Path(__file__).parent / "videos" / "vid1.mp4").__str__()

video = cv2.VideoCapture(VIDEO_PATH)
pose = mp.solutions.pose
mp_pose = pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils


def get_cords(attr:str) -> tuple[int, int]:
    return (int(points.landmark[getattr(pose.PoseLandmark, attr)].x * width), int(points.landmark[getattr(pose.PoseLandmark, attr)].y * height))




def run():
    if right_hand_x < right_elbow_x or left_hand_x > left_elbow_x:
        print("CORRENDO")
    else:
        print("Repouso")
        

while True:
    success, img = video.read()
    
    video_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = mp_pose.process(video_rgb)
    points = results.pose_landmarks
    
        
    mp_draw.draw_landmarks(img, points, pose.POSE_CONNECTIONS)
    
    
    height, width, _ = img.shape
    
    if points:
        right_hand_x, right_hand_y = get_cords("RIGHT_INDEX")
        left_hand_x, left_hand_y= get_cords("LEFT_INDEX")
        right_elbow_x, right_elbow_y = get_cords("RIGHT_ELBOW")
        left_elbow_x, left_elbow_y = get_cords("LEFT_ELBOW")
        right_shoulder_x, right_shoulder_y = get_cords("RIGHT_SHOULDER")
        left_shoulder_x, left_shoulder_y  = get_cords("LEFT_SHOULDER")
        nose_x, nose_y = get_cords("NOSE")
        
        # Calcular a distância entre a mão direita e o ombro direito
        dist_maoDireita_ombro = int(math.hypot(right_hand_x - right_shoulder_x, right_hand_y - right_shoulder_y))
        
        dist_maoDireita_ombro = int(math.hypot(right_hand_x - right_elbow_x, right_hand_y - right_elbow_y))

        #print(f"X_Cotovovelo: {right_elbow_x}, X_RHand: {right_hand_x}")
        run()

        # Desenhar uma linha na altura do nariz
        cv2.line(img, (0, nose_y), (width, nose_y), (0, 255, 0), 1)

        # Desenhar uma linha vertical sobre o cotovelo direito
        cv2.line(img, (right_elbow_x, 0), (right_elbow_x, height), (0, 255, 0), 1)

    cv2.imshow("Image", img)
    cv2.waitKey(10)
