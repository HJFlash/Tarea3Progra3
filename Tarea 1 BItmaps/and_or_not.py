from PIL import Image, ImageChops

# Abrir dos imágenes
Img1 = Image.open('Imagen1.png').convert('1')  # Convertir a blanco y negro
Img2 = Image.open('Imagen2.png').convert('1')  # Convertir a blanco y negro

# Operación AND
OperacionAND = ImageChops.difference(Img1, Img2).point(lambda x: x > 0 and 255)
OperacionAND.show()

# Operación OR
OperacionOR = ImageChops.logical_or(Img1, Img2)
OperacionOR.show()

# Operación NOT
OperacionNOT = ImageChops.invert(Img1)
OperacionNOT.show()
