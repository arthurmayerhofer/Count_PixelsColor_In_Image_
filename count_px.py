import cv2
import numpy as np

# leitura da imagem
img = cv2.imread('C:/Syngenta.bmp')

# cor verde encontrada na imagem
green = np.array([0, 192, 96], np.uint8)
# variável para armezenar a quantidade de pixels
green_pixels = 0

# Faixa de cores verde para a contagem dos pixels
min_green = np.array([0, 180, 80], np.uint8)
max_green = np.array([10, 210, 120], np.uint8)
dst = cv2.inRange(img, min_green, max_green)

# Primeiro método com
# função de contagem dos pixels com cores correspondentes à faixa
count_green = cv2.countNonZero(dst)

# função para percorrer os pixels da imagem
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        # valor rgb dos pixels
        v = img[i, j]
        # Verificação do primeiro método de contagem com
        # condição para pintar pixels verdes de preto
        if np.all(v == green, axis=-1):
            img[i, j, 0] = 0
            img[i, j, 1] = 0
            img[i, j, 2] = 0
            # incrementa pixels verdes na variável
            green_pixels += 1

# Comparação dos dois métodos de contagem
if count_green == green_pixels:
    print("A quantidade de pixels verdes é  " + str(green_pixels))

cv2.imshow('Imagem sem Verde', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
