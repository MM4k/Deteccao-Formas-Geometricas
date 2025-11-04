import cv2
import numpy as np

def nothing(x):
    pass

# Interface
cv2.namedWindow("Controles HSV")
cv2.resizeWindow("Controles HSV", 600, 300)

# Limites mínimos de HSV
cv2.createTrackbar("H Min", "Controles HSV", 0, 179, nothing)
cv2.createTrackbar("S Min", "Controles HSV", 0, 255, nothing)
cv2.createTrackbar("V Min", "Controles HSV", 0, 255, nothing)

# Limites máximos de HSV
cv2.createTrackbar("H Max", "Controles HSV", 179, 179, nothing)
cv2.createTrackbar("S Max", "Controles HSV", 255, 255, nothing)
cv2.createTrackbar("V Max", "Controles HSV", 255, 255, nothing)

video_path = 'assets/video_desafio_1.mp4' 
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    exit()

is_paused = False
frame = None

while True:
    key = cv2.waitKey(30) & 0xFF
    if key == ord(' '): # Pressionar 'espaço' para pausar/despausar
        is_paused = not is_paused

    if not is_paused:
        ret, current_frame = cap.read()
        if not ret:
            # Reiniciar o vídeo quando acabar
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue
        
        # Armazena o frame lido para ser processado
        frame = current_frame

    if frame is None:
        continue
    
    # Converter de BGR para HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Leitura dos valores
    h_min = cv2.getTrackbarPos("H Min", "Controles HSV")
    s_min = cv2.getTrackbarPos("S Min", "Controles HSV")
    v_min = cv2.getTrackbarPos("V Min", "Controles HSV")
    h_max = cv2.getTrackbarPos("H Max", "Controles HSV")
    s_max = cv2.getTrackbarPos("S Max", "Controles HSV")
    v_max = cv2.getTrackbarPos("V Max", "Controles HSV")

    # Arrays de limites
    lower_bound = np.array([h_min, s_min, v_min])
    upper_bound = np.array([h_max, s_max, v_max])
    
    # Máscara binária
    color_mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)
    
    # Exibição
    cv2.imshow("Video Original", frame)
    cv2.imshow("Mascara (Debug)", color_mask)