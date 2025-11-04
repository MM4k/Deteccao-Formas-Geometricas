import cv2
import numpy as np

# Parametrização Central
BLUR_KERNEL_SIZE = (5, 5)   # Tamanho do kernel para o GaussianBlur
MIN_CONTOUR_AREA = 1000     # Área mínima para detectar uma forma

SHAPE_DATABASE = {
    "CIRCULO": {
        'color_label': "Azul",
        'lower': np.array([103, 102, 169]), 
        'upper': np.array([112, 147, 255])
    },
    "QUADRADO": {
        'color_label': "Marrom Escuro",
        'lower': np.array([114, 27, 90]), 
        'upper': np.array([147, 61, 140])
    },
    "TRIANGULO": {
        'color_label': "Azul Escuro",
        'lower': np.array([109, 75, 122]), 
        'upper': np.array([113, 134, 192])
    },
    "PENTAGONO": {
        'color_label': "Vinho",
        'lower': np.array([160, 85, 171]), 
        'upper': np.array([179, 255, 226])
    },
    "CRUZ": {
        'color_label': "Magenta",
        'lower': np.array([143, 75, 163]), 
        'upper': np.array([158, 185, 255])
    },
    "ESTRELA": {
        'color_label': "Verde",
        'lower': np.array([49, 34, 42]), 
        'upper': np.array([89, 83, 255])
    },
    "CASA": { # Pentágono Irregular
        'color_label': "Laranja",
        'lower': np.array([166, 38, 155]),
        'upper': np.array([179, 255, 255])
    },
    "HEXAGONO": {
        'color_label': "Vermelho",
        'lower': np.array([162, 199, 146]),
        'upper': np.array([179, 255, 255])
    }
}

video_path = 'assets/video_desafio_1.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # 1. Pré-processamento
    blurred_frame = cv2.GaussianBlur(frame, BLUR_KERNEL_SIZE, 0)
    hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
    result_frame = frame.copy()

    # 2. Loop de Detecção (para cada forma no nosso BD)
    for shape_name, properties in SHAPE_DATABASE.items():
        # Pula formas que ainda não foram calibradas
        if np.array_equal(properties['lower'], np.array([0, 0, 0])):
            continue

        # 3. Segmentação por Cor
        lower_bound = properties['lower']
        upper_bound = properties['upper']
        color_mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

        # 4. Análise de Contornos
        contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > MIN_CONTOUR_AREA:
                M = cv2.moments(cnt)
                if M["m00"] == 0: continue
                
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                
                # Visualização
                cv2.drawContours(result_frame, [cnt], -1, (0, 0, 255), 2)
                text = f"{shape_name} ({properties['color_label']})"
                cv2.putText(result_frame, text, (cX - 60, cY), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # 5. Exibição dos Resultados
    cv2.imshow("Detector de Formas (Estavel)", result_frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()