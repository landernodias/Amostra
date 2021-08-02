import numpy as np
import cv2

#carrega as imagens
img = cv2.imread('teste.png')
image = cv2.imread('teste01.png')
output = image.copy()

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#converte em tons de cinza
#rows = img.shape[0]

#funçãoHough
#circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, rows/17, param1=60, param2=10, minRadius=10, maxRadius=37)
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 40, param1=50, param2=12, minRadius=10, maxRadius=37)

#Exibe detecção
detected_circles = np.uint16(np.around(circles))
for (x,y,r) in detected_circles[0, :]:
    #cv2.circle(output, (x, y), r,(0,255,0),1)
    #cv2.circle(output, (x, y), 2,(0,0,255),r)
    cv2.circle(output, (x, y), r,(0,255,0),1)
    cv2.circle(output, (x, y), 2,(0,255,0),2)
#Mostra na tela
cv2.imshow('img_Entrada',output)
cv2.imshow('img_pivodetec',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#information Hough circles transform 

#imagem:	        Imagem de entrada em tons de cinza de canal único, 8 bits.
#circles:	        Vetor de saída dos círculos encontrados (tipo cv.CV_32FC3). Cada vetor é codificado como um vetor de ponto flutuante de 3 elementos (x, y, raio).
#HOUGD_GRADIENT:	Método de detecção (consulte cv.HoughModes ). Atualmente, o único método implementado é HOUGH_GRADIENT
#dp:	            Razão inversa da resolução do acumulador para a resolução da imagem. Por exemplo, se dp = 1, o acumulador tem a mesma resolução da imagem de entrada. Se dp = 2, o acumulador tem metade da largura e da altura.
#minDist:	        Distância mínima entre os centros dos círculos detectados. Se o parâmetro for muito pequeno, vários círculos vizinhos podem ser detectados falsamente, além de um verdadeiro. Se for muito grande, alguns círculos podem ser perdidos.
#param1:	        Primeiro parâmetro específico do método. No caso de HOUGH_GRADIENT, é o limite superior dos dois passado para o detector de borda do Canny (o inferior é duas vezes menor).
#param2:	        Segundo parâmetro específico do método. No caso de HOUGH_GRADIENT, é o limite do acumulador para os centros do círculo no estágio de detecção. Quanto menor for, mais círculos falsos podem ser detectados. Círculos, correspondentes aos maiores valores do acumulador, serão retornados primeiro.
#minRadius:	        Raio mínimo do círculo.
#maxRadius:	        Raio máximo do círculo.  
