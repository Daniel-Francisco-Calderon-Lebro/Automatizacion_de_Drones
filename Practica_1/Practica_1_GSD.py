import cv2 as cv

# Cargar imagen
img = cv.imread(r'Practica_1\DJI_0850.JPG', 1)
print(img.shape)

h = 60000 - 12000 # Altura en mm
imw = 4000 # Ancho de la imagen en pixeles
Sw = 6.3 #Ancho del sensor de la camara en mm
F = 4.44 # Distancia focal en mm

# Calcular GSD
gsd_mm = ((h/imw) * (Sw/F)) # mm/pixel en horizontal
print("GSD: ", gsd_mm, "mm/pixel")
gsd_cm = gsd_mm/10 # cm/pixel en horizontal
print("GSD: ", gsd_cm, "cm/pixel")
gsd_m = gsd_mm/1000 # m/pixel en horizontal
print("GSD: ", gsd_m, "m/pixel")

# Altura de vuelo en metros
h_mm = gsd_mm * imw * (F/Sw)
h_cm = h_mm/10
h_m = h_mm/1000
# h_m = (imw*gsdw/100) *F / (sw*10)
print("Altura de vuelo: ", h_mm, "mm")
print("Altura de vuelo: ", h_cm, "cm")
print("Altura de vuelo: ", h_m, "m")


# recorte total de toda la imagen
recorte = img[979:2185, 107:3673] # (y1:y2, x1:x2) Ajustar coordenadas manualmente


print(recorte.shape)
# Medida horizontal
largo = len(recorte[0])
print(largo)
medida_horizontal_mm = largo * gsd_mm
medida_horizontal_cm = medida_horizontal_mm / 10
medida_horizontal_m = medida_horizontal_mm / 1000 
print(medida_horizontal_mm)

# Medida vertical
ancho = len(recorte)
print(ancho)
medida_vertical_mm = ancho * gsd_mm
medida_vertical_cm = medida_vertical_mm / 10
medida_vertical_m = medida_vertical_mm / 1000
print(medida_vertical_mm)

#ventana normal
cv.namedWindow("recorte", cv.WINDOW_NORMAL)
cv.rectangle(recorte, (0, 0), (largo, ancho), (0, 255, 0), 32)
cv.putText(recorte, "Largo: " + str(round(float(medida_horizontal_m), 2)) + " m", (1000, 120), cv.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 255), 16)
cv.putText(recorte, "Ancho: " + str(round(float(medida_vertical_m), 2)) + " m", (20, 700), cv.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 255), 16)

# Ventana de imagenes
cv.namedWindow("imagen", cv.WINDOW_NORMAL)
cv.imshow("imagen", img)
cv.imshow("recorte", recorte)
cv.waitKey(0)
cv.destroyAllWindows()