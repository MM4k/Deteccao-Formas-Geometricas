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

image_path = 'assets/13_frame_000004_t6.00s.jpg' 
frame = cv2.imread(image_path)

if frame is None:
    exit()

hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
cv2.imshow("Imagem Original", frame)

while True:
    
    # --- Leitura dos Valores da UI (em tempo real) ---
    h_min = cv2.getTrackbarPos("H Min", "Controles HSV")
    s_min = cv2.getTrackbarPos("S Min", "Controles HSV")
    v_min = cv2.getTrackbarPos("V Min", "Controles HSV")
    h_max = cv2.getTrackbarPos("H Max", "Controles HSV")
    s_max = cv2.getTrackbarPos("S Max", "Controles HSV")
    v_max = cv2.getTrackbarPos("V Max", "Controles HSV")

    # Criar os arrays de limites
    lower_bound = np.array([h_min, s_min, v_min])
    upper_bound = np.array([h_max, s_max, v_max])
    
    # Criar a máscara binária (em tempo real)
    color_mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)
    
    # Exibição da máscara
    cv2.imshow("Mascara (Debug)", color_mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()