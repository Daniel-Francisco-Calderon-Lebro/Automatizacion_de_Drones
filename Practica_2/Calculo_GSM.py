
#26.855m mide la altura del edificio
altura_edificio = 26855 # Altura en mm
h = 86900 - altura_edificio # Altura en mm del Dron
imw = 5472 # Ancho de la imagen en pixeles
imh = 3648 # Alto de la imagen en pixeles
Sw = 13.2 #Ancho del sensor de la camara en mm
Sh = 8 # Alto del sensor de la camara en mm
F = 8.8 # Distancia focal en mm

# Calcular GSD
gsd_mm = ((h/imw) * (Sw/F)) # mm/pixel en horizontal
gsd_mm_vertical = ((h/imh) * (Sh/F)) # mm/pixel en vertical
print("GSD: ", gsd_mm, "mm/pixel en horizontal")
print("GSD: ", gsd_mm_vertical, "mm/pixel en vertical")
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
